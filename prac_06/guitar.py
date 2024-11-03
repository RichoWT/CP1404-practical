"""
CP1404
Time estimated: 30 minutes ( 3:07pm )
Time finished:
"""

YEAR = 2024
VINTAGE_AGE = 50

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return YEAR - self.year

    def is_vintage(self):
        return self.get_age() > VINTAGE_AGE