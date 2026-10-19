from datetime import datetime
from typing import List

import pytest

from lld.booking_system import BookingSystem
from lld.movie import Movie
from lld.showtime import Showtime
from lld.theatre import Theatre

SEATS: List[str] = ["A1", "A2", "A3", "A4", "A5"]


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
