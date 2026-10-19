
from lld.movie_theatre.movie import Movie
from lld.movie_theatre.reservation import Reservation
from lld.movie_theatre.showtime import Showtime
from lld.movie_theatre.theatre import Theatre


class BookingSystem:
    def __init__(self, theatres: list[Theatre]) -> None:
        self._theatres: list[Theatre] = theatres
        
        # quick access dictionaries
        self._movies_by_id: dict[str, Movie] = {}
        self._showtimes_by_movie_id: dict[str, list[Showtime]] = {}
        self._showtimes_by_id: dict[str, Showtime] = {}
        self._reservations_by_id: dict[str, Reservation] = {}

    def search_movies(self, title: str) -> list[Showtime]:
        
        showtimes = []
        
        for theatre in self._theatres:
            for showtime in theatre._showtimes:
                if title in showtime.get_movie():
                    showtimes = showtime
                    
        return showtimes

    def get_showtimes_at_theatre(self, theatre: Theatre) -> list[Showtime]:
        raise NotImplementedError

    def book(self, showtime: Showtime, seat_ids: list[str]) -> Reservation:
        raise NotImplementedError

    def get_reservation(self, confirmation_id: str) -> Reservation:
        raise NotImplementedError

    def cancel_reservation(self, confirmation_id: str) -> None:
        raise NotImplementedError
