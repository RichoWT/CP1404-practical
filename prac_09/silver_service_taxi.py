
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness, price_per_km):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = price_per_km

    def get_fare(self):
        return self.flagfall + super().get_fare()





