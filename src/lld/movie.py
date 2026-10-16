class Movie:
    def __init__(self, movie_id: str, title: str) -> None:
        self._id: str = movie_id
        self._title: str = title

    def get_id(self) -> str:
        return self._id

    def get_title(self) -> str:
        return self._title
