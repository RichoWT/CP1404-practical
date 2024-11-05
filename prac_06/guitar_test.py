"""
CP1404
Time estimated: 30 minutes ( 3:07pm )
Time finished: 57 minutes (4:04pm)
"""

from prac_06.guitar import Guitar

YEAR = 2024

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
other = Guitar("Another Guitar", 2013, 1825.5)

print(f"{guitar.name} get_age() - Expected {102}. Got {guitar.get_age()}")
print(f"{other.name} get_age() - Expected {11}. Got {other.get_age()}")
print()
print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")
