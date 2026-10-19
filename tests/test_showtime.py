import threading

import pytest

from lld.movie_theatre.showtime import Showtime
from tests.conftest import SEATS


def test_all_seats_available_initially(showtime: Showtime) -> None:
    assert showtime.get_available_seats() == SEATS
    assert showtime.is_available("A1")


def test_book_returns_reservation_with_seats(showtime: Showtime) -> None:
    reservation = showtime.book(["A1", "A2"])

    assert reservation.get_seat_ids() == ["A1", "A2"]
    assert reservation.get_showtime() is showtime
    assert reservation.get_confirmation_id()


def test_booked_seats_become_unavailable(showtime: Showtime) -> None:
    showtime.book(["A1", "A2"])

    assert not showtime.is_available("A1")
    assert showtime.get_available_seats() == ["A3", "A4", "A5"]


def test_confirmation_ids_are_unique(showtime: Showtime) -> None:
    first = showtime.book(["A1"])
    second = showtime.book(["A2"])

    assert first.get_confirmation_id() != second.get_confirmation_id()


def test_booking_already_booked_seat_raises(showtime: Showtime) -> None:
    showtime.book(["A1"])

    with pytest.raises(ValueError):
        showtime.book(["A1"])


def test_booking_is_all_or_nothing(showtime: Showtime) -> None:
    showtime.book(["A2"])

    with pytest.raises(ValueError):
        showtime.book(["A1", "A2"])  # A2 is taken, so A1 must not be booked either

    assert showtime.is_available("A1")


@pytest.mark.parametrize("bad_seats", [[], ["Z9"], ["A1", "A1"]])
def test_invalid_seat_requests_raise(showtime: Showtime, bad_seats: list[str]) -> None:
    # empty request, unknown seat, duplicate seat in one request
    with pytest.raises(ValueError):
        showtime.book(bad_seats)


def test_cancel_frees_seats(showtime: Showtime) -> None:
    reservation = showtime.book(["A1", "A2"])

    showtime.cancel(reservation.get_confirmation_id())

    assert showtime.get_available_seats() == SEATS


def test_cancel_unknown_confirmation_raises(showtime: Showtime) -> None:
    with pytest.raises(KeyError):
        showtime.cancel("nope")


def test_cancel_twice_raises(showtime: Showtime) -> None:
    reservation = showtime.book(["A1"])
    showtime.cancel(reservation.get_confirmation_id())

    with pytest.raises(KeyError):
        showtime.cancel(reservation.get_confirmation_id())


def test_concurrent_booking_of_same_seat_exactly_one_succeeds(showtime: Showtime) -> None:
    results: list[bool] = []
    barrier = threading.Barrier(20)  # makes all threads start booking at the same moment

    def try_book() -> None:
        barrier.wait()
        try:
            showtime.book(["A1"])
            results.append(True)
        except ValueError:
            results.append(False)

    threads = [threading.Thread(target=try_book) for _ in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert results.count(True) == 1
    assert results.count(False) == 19
