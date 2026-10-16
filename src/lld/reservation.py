from __future__ import annotations  # lets us reference Showtime in type hints without a circular import

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:  # only imported for type checkers, never at runtime
    from lld.showtime import Showtime


class Reservation:
    def __init__(self, confirmation_id: str, showtime: Showtime, seat_ids: List[str]) -> None:
        self._confirmation_id: str = confirmation_id
        self._showtime: Showtime = showtime
        self._seat_ids: List[str] = seat_ids

    def get_confirmation_id(self) -> str:
        return self._confirmation_id

    def get_seat_ids(self) -> List[str]:
        return list(self._seat_ids)

    def get_showtime(self) -> Showtime:
        return self._showtime
