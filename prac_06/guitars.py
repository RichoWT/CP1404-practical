"""
CP1404
Time estimated: 30 minutes ( 3:07pm )
Time finished:
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_to_add = Guitar(name, year, cost)
    guitars.append(guitar_to_add)
    print(f"{guitar_to_add} added.")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

if guitars:
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (Vintage)"
        print(f"Guitar {i+1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
else:
    print("No guitars")