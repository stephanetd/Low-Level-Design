from aircraft import Aircraft
from payment_processor import PaymentProcessor
from booking_manager import BookingManager
from flight_search import FlightSearch
from flight import Flight

class AirlineManagementSystem:
    def __init__(self):
        self.flights = []
        self.aircrafts = []
        self.booking_manager = BookingManager()
        self.flight_search = FlightSearch()
        self.payment_processor = PaymentProcessor

    def add_flight(self, flight: Flight):
        self.flights.append(flight)

    def add_aircraft(self, aircraft: Aircraft):
        self.aircrafts.append(aircraft)

    def search_flights(self, source, destination, search_date):
        pass

    def book_flight(self, flight, passenger, seat, price):
        self.booking_manager.create_booking(flight, passenger, seat, price)

    def cancel_booking(self, booking_number):
        self.booking_manager.cancel_booking(booking_number)

    def process_payment(self, payment):
        self.payment_processor.process_payment(payment)
