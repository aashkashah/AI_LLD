from datetime import datetime

from lld.movie import Movie
from lld.showtime import Showtime
from lld.theatre import Theatre


def test_new_theatre_has_no_showtimes(theatre: Theatre) -> None:
    assert theatre.get_showtimes() == []


def test_add_showtime_makes_it_visible(theatre: Theatre, showtime: Showtime) -> None:
    theatre.add_showtime(showtime)

    assert theatre.get_showtimes() == [showtime]


def test_get_showtimes_returns_a_copy(theatre: Theatre, showtime: Showtime) -> None:
    theatre.add_showtime(showtime)

    theatre.get_showtimes().clear()

    assert theatre.get_showtimes() == [showtime]


def test_get_showtimes_for_movie_filters_by_movie(
    theatre: Theatre, showtime: Showtime, matrix: Movie
) -> None:
    other = Showtime("s2", theatre, datetime(2026, 11, 1, 21, 0), "Screen 2", matrix, ["B1"])
    theatre.add_showtime(showtime)
    theatre.add_showtime(other)

    assert theatre.get_showtimes_for_movie(matrix) == [other]


def test_get_showtimes_for_movie_with_no_match_is_empty(
    theatre: Theatre, showtime: Showtime, matrix: Movie
) -> None:
    theatre.add_showtime(showtime)

    assert theatre.get_showtimes_for_movie(matrix) == []
