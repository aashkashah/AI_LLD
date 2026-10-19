
Requirements 
A theatre booking system
    actions by user - 
        search tickets by movie name 
        browse movies playing at a theatre

        view available seats
        book ticket(s) - selection based, success returns a reservation number  
        get reservation
        cancel reservation  
        concurrent booking of the same seat -> exactly one succeeds

out of scope 

    payment processing (assume payment always succeeds)
    variable seat layouts or seat types (all seat identical)
    rescheduling (cancel and rebook instead)
    UI / rendering


Entities 
BookingSystem (Type: class)
    Orchestrator, owns theatre. Entry point for search and cross-theatre queries 

Movie (Type: class)
    Searchable entity. Title plus Id. Ties showtime together across theatres

Theatre (Type: class)
    Name location. Owns a list of showtimes

Showtime (Type: class)
    A specific screeing. Tracks per-seat availability and handles 
    booking concurrency

Reservation (Type: class)
    User's booking reference. Stores confirmation Id and which seats were booked. Used for cancellation

Seat (Type: string)
    A string identifying a specific seat, e.g. "A5". No behavior, just an identifier.

Screen (Type: string)
    Label identifying which room a showtime is in, e.g. "Screen 3".
