def can_book_room(attendees: int, capacity: int, allow_standing: bool = False) -> bool:
    if attendees < 0:
        raise ValueError("attendees must be non-negative")
    if capacity <= 0:
        raise ValueError("capacity must be positive")

    limit = capacity + 2 if allow_standing else capacity
    # Allow bookings that are exactly at the computed limit.
    return attendees <= limit
