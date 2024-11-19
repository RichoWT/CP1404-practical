from random import randint
from prac_09.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        super().__init__(name)

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_drove = super().drive(distance)
        return distance_drove
