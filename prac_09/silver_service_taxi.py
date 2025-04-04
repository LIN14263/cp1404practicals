# silver_service_taxi.py
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A fancy taxi with additional flagfall and fanciness scaling."""
    flagfall = 4.50  # 类变量，每次新行程的附加费

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness  # 根据fanciness调整价格

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate the fare including flagfall."""
        return round(super().get_fare() + self.flagfall, 1)  # 按要求四舍五入到10分