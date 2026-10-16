from typing import List

from lld.reservation import Reservation
from lld.showtime import Showtime
from lld.theatre import Theatre


class BookingSystem:
    def __init__(self, theatres: List[Theatre]) -> None:
        self._theatres: List[Theatre] = theatres

    def search_movies(self, title: str) -> List[Showtime]:
        raise NotImplementedError

    def get_showtimes_at_theatre(self, theatre: Theatre) -> List[Showtime]:
        raise NotImplementedError

    def book(self, showtime: Showtime, seat_ids: List[str]) -> Reservation:
        raise NotImplementedError

    def get_reservation(self, confirmation_id: str) -> Reservation:
        raise NotImplementedError

    def cancel_reservation(self, confirmation_id: str) -> None:
        raise NotImplementedError
