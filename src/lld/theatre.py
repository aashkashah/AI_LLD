
from lld.movie import Movie
from lld.showtime import Showtime


class Theatre:
    def __init__(self, theatre_id: str, name: str) -> None:
        self._id: str = theatre_id
        self._name: str = name
        self._showtimes: list[Showtime] = []

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def add_showtime(self, showtime: Showtime) -> None:
        raise NotImplementedError

    def get_showtimes(self) -> list[Showtime]:
        raise NotImplementedError

    def get_showtimes_for_movie(self, movie: Movie) -> list[Showtime]:
        raise NotImplementedError
