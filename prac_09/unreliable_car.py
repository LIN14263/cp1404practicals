# unreliable_car.py
from car import Car
import random

class UnreliableCar(Car):
    """A car that may or may not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability  # 0-100之间的浮点数

    def drive(self, distance):
        """Drive only if a random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0  # 如果不可靠，返回0