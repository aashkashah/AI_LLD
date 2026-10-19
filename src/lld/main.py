from datetime import datetime

from lld.booking_system import BookingSystem
from lld.movie import Movie
from lld.showtime import Showtime
from lld.theatre import Theatre


def main() -> None:
    # Set up some sample data.
    inception = Movie("m1", "Inception")
    theatre = Theatre("t1", "PVR Downtown")
    showtime = Showtime(
        "s1", theatre, datetime(2026, 11, 1, 18, 0), "Screen 1", inception, ["A1", "A2", "A3", "A4", "A5"]
    )
    theatre.add_showtime(showtime)
    system = BookingSystem([theatre])

    # Walk through the user actions from requirements.md.
    print("Search 'incep':", [s.get_id() for s in system.search_movies("incep")])
    print("Available seats:", showtime.get_available_seats())

    reservation = system.book(showtime, ["A1", "A2"])
    print("Booked, confirmation id:", reservation.get_confirmation_id())
    print("Available seats:", showtime.get_available_seats())

    system.cancel_reservation(reservation.get_confirmation_id())
    print("After cancel:", showtime.get_available_seats())


# Like C#'s `static void Main`: runs only when this file is executed directly.
if __name__ == "__main__":
    main()
