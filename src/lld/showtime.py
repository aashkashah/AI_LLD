from __future__ import annotations

import threading
from datetime import datetime
from typing import TYPE_CHECKING

from lld.movie import Movie
from lld.reservation import Reservation

if TYPE_CHECKING:
    from lld.theatre import Theatre


class Showtime:
    def __init__(
        self,
        showtime_id: str,
        theatre: Theatre,
        start_time: datetime,
        screen_label: str,
        movie: Movie,
        all_seat_ids: list[str],
    ) -> None:
        self._id: str = showtime_id
        self._theatre: Theatre = theatre
        self._start_time: datetime = start_time
        self._screen_label: str = screen_label
        self._movie: Movie = movie
        self._all_seat_ids: list[str] = all_seat_ids
        self._reservations: list[Reservation] = []
        # Guards booking/cancel so two users can't take the same seat (≈ C# lock object).
        self._lock: threading.Lock = threading.Lock()

    def get_id(self) -> str:
        return self._id

    def get_theatre(self) -> Theatre:
        return self._theatre

    def get_start_time(self) -> datetime:
        return self._start_time

    def get_screen_label(self) -> str:
        return self._screen_label

    def get_movie(self) -> Movie:
        return self._movie

    def is_available(self, seat_id: str) -> bool:
        raise NotImplementedError

    def get_available_seats(self) -> list[str]:
        raise NotImplementedError

    def book(self, seat_ids: list[str]) -> Reservation:
        raise NotImplementedError

    def cancel(self, confirmation_id: str) -> None:
        raise NotImplementedError
