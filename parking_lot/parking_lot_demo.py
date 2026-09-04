from parking_lot import ParkingLot
from level import Level
from car import Car
from motorcycle import Motorcycle
from truck import Truck

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 5))
        parking_lot.add_level(Level(2, 3))

        car = Car("ABC123")
        truck = Truck("XYZ789")
        motorcycle = Motorcycle("M1234")

        # Display availability
        print("After creation.")
        parking_lot.display_availability()


        # Park vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)

        print("\nAfter parking 3 vehicles.")
        # Display availability
        parking_lot.display_availability()


        # Unpark vehicle
        parking_lot.unpark_vehicle(car)

        print("\nAfter freeing one spot.")
        # Display updated availability
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()