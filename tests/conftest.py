from datetime import datetime

import pytest

from lld.movie_theatre.booking_system import BookingSystem
from lld.movie_theatre.movie import Movie
from lld.movie_theatre.showtime import Showtime
from lld.movie_theatre.theatre import Theatre

SEATS: list[str] = ["A1", "A2", "A3", "A4", "A5"]


# Fixtures are like injected test dependencies: pytest passes them in by parameter name.
@pytest.fixture
def theatre() -> Theatre:
    return Theatre("t1", "PVR Downtown")


@pytest.fixture
def inception() -> Movie:
    return Movie("m1", "Inception")


@pytest.fixture
def matrix() -> Movie:
    return Movie("m2", "The Matrix")


@pytest.fixture
def showtime(theatre: Theatre, inception: Movie) -> Showtime:
    return Showtime("s1", theatre, datetime(2026, 11, 1, 18, 0), "Screen 1", inception, list(SEATS))


@pytest.fixture
def system(theatre: Theatre, showtime: Showtime) -> BookingSystem:
    theatre.add_showtime(showtime)
    return BookingSystem([theatre])
