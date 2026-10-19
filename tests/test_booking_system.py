from datetime import datetime

import pytest

from lld.movie_theatre.booking_system import BookingSystem
from lld.movie_theatre.movie import Movie
from lld.movie_theatre.showtime import Showtime
from lld.movie_theatre.theatre import Theatre


def test_search_movies_finds_showtimes_across_theatres(system: BookingSystem, showtime: Showtime, inception: Movie) -> None:
    other_theatre = Theatre("t2", "Cinepolis")
    other_showtime = Showtime("s9", other_theatre, datetime(2026, 11, 2, 20, 0), "Screen 4", inception, ["A1"])
    other_theatre.add_showtime(other_showtime)
    both = BookingSystem([showtime.get_theatre(), other_theatre])

    result = both.search_movies("Inception")

    assert set(result) == {showtime, other_showtime}


def test_search_movies_is_case_insensitive_partial_match(system: BookingSystem, showtime: Showtime) -> None:
    assert system.search_movies("incep") == [showtime]
    assert system.search_movies("INCEPTION") == [showtime]


def test_search_movies_no_match_returns_empty(system: BookingSystem) -> None:
    assert system.search_movies("Titanic") == []


def test_get_showtimes_at_theatre(system: BookingSystem, theatre: Theatre, showtime: Showtime) -> None:
    assert system.get_showtimes_at_theatre(theatre) == [showtime]


def test_book_returns_reservation_and_holds_seats(system: BookingSystem, showtime: Showtime) -> None:
    reservation = system.book(showtime, ["A1", "A2"])

    assert reservation.get_seat_ids() == ["A1", "A2"]
    assert not showtime.is_available("A1")


def test_get_reservation_by_confirmation_id(system: BookingSystem, showtime: Showtime) -> None:
    reservation = system.book(showtime, ["A1"])

    found = system.get_reservation(reservation.get_confirmation_id())

    assert found is reservation


def test_get_unknown_reservation_raises(system: BookingSystem) -> None:
    with pytest.raises(KeyError):
        system.get_reservation("nope")


def test_cancel_reservation_frees_seats(system: BookingSystem, showtime: Showtime) -> None:
    reservation = system.book(showtime, ["A1", "A2"])

    system.cancel_reservation(reservation.get_confirmation_id())

    assert showtime.is_available("A1")
    assert showtime.is_available("A2")


def test_cancelled_reservation_can_no_longer_be_fetched(system: BookingSystem, showtime: Showtime) -> None:
    reservation = system.book(showtime, ["A1"])
    system.cancel_reservation(reservation.get_confirmation_id())

    with pytest.raises(KeyError):
        system.get_reservation(reservation.get_confirmation_id())


def test_cancel_unknown_reservation_raises(system: BookingSystem) -> None:
    with pytest.raises(KeyError):
        system.cancel_reservation("nope")


def test_seat_can_be_rebooked_after_cancel(system: BookingSystem, showtime: Showtime) -> None:
    first = system.book(showtime, ["A1"])
    system.cancel_reservation(first.get_confirmation_id())

    second = system.book(showtime, ["A1"])

    assert second.get_seat_ids() == ["A1"]
