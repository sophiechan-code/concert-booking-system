from .user import Fan
from .concert import Concert
from datetime import datetime


class Booking:

    total_bookings = 0
    
    def __init__(self, fan: Fan, concert: Concert):
        self._fan = fan
        self._concert = concert
        self._booking_id = f"Booking-{Booking.total_bookings + 1:04d}"
        self._timestamp = datetime.now()
        
        Booking.total_bookings += 1

    def get_fan(self) -> Fan:
        return self._fan

    def set_fan(self, fan: Fan):
        self._fan = fan

    def get_concert(self) -> Concert:
        return self._concert

    def set_concert(self, concert: Concert):
        self._concert = concert

    def get_booking_id(self) -> str:
        return self._booking_id

    def set_booking_id(self, booking_id: str):
        self._booking_id = booking_id

    def __lt__(self, other: 'Booking') -> bool:
        if self._fan.get_priority() == other._fan.get_priority():
            return self._timestamp > other._timestamp
            
        return self._fan.get_priority() < other._fan.get_priority()

    def __eq__(self, other: 'Booking') -> bool:
        return self._booking_id == other._booking_id

    def __str__(self) -> str:
        return f"[{self._booking_id}] {self._fan.get_name()} (Priority {self._fan.get_priority()}) booked {self._concert.get_artist().get_name()}"
