# taxi.py
from car import Car

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # 类变量

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation of a Taxi."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Calculate the fare based on distance driven."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Reset the meter for a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive the taxi and update fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven