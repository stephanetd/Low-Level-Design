from vehicle import Vehicle
from vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self, spot_number: int):
        self.spot_num = spot_number
        self.parked_vehicle = None
        self.vehicle_type = VehicleType.CAR # by default

    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.is_available() and self.vehicle_type == vehicle.get_vehicle_type():
            self.parked_vehicle = vehicle
        else:
            raise Exception("Invalid vehicle type or parking spot already occupied!")

    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def get_spot_num(self) -> int:
        return self.spot_num

    def get_parked_vehicle(self) -> Vehicle|None:
        return self.parked_vehicle

    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type