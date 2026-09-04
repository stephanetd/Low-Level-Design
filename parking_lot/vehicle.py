from vehicle_type import VehicleType
from abc import ABC
class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type):
        self.license_plate = license_plate
        self.type = vehicle_type # type is car by default

    def get_license_plate(self) -> str:
        return self.license_plate

    def get_vehicle_type(self) -> VehicleType:
        return self.type