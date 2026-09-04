from threading import Lock
from booking import Booking
import datetime

class BookingManager:
    _instance = None
    _lock = Lock
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.bookings = {}
        self.booking_counter = 0

    def create_booking(self, flight, passenger, seat, price) -> Booking:
        booking_number = self._generate_booking_number()
        booking = Booking(flight, passenger, seat, price)
        with self._lock:
            self.bookings[booking_number] = booking
        return booking

    def cancel_booking(self, booking_number) -> None:
        with self._lock:
            booking = self.bookings[booking_number]
            if booking:
                booking.cancel()
                del self.bookings[booking_number]


    def _generate_booking_number(self):
        self.booking_counter += 1
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"BKG{timestamp}{self.booking_counter:06d}"