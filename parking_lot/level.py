from typing import List

from vehicle import Vehicle
from parking_spot import ParkingSpot

class Level:
    def __init__(self, floor_number, num_parking_spots):
        self.floor = floor_number
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(num_parking_spots)]
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_full():
            return False
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_vehicle_type():
                spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False

    def is_full(self) -> bool:
        for parking_spot in self.parking_spots:
            if parking_spot.is_available():
                return False
        return True

    def display_availability(self):
        print(f"\nLevel {self.floor} Availability:")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_num()}: {'Available' if spot.is_available() else 'Occupied'}")
