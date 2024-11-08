import csv
from prac_07.guitar import Guitar


def main():
    filename = 'guitar.csv'
    guitars = load_guitars_from_csv(filename)
    guitars.sort()
    show_guitars(guitars)
    get_new_guitar(guitars)
    save_guitars(filename, guitars)


def load_guitars_from_csv(filename):
    guitars = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                name, year, cost = row
                guitars.append(Guitar(name.strip(), int(year), float(cost)))
    return guitars


def show_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def get_new_guitar(guitars):
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ").strip()


def save_guitars(filename, guitars):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


main()
