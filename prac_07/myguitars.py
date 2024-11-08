import csv
from prac_07.guitar import Guitar


def main():
    filename = 'guitar.csv'
    guitars = load_guitars_from_csv(filename)
    guitars.sort()
    show_guitars(guitars)


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


main()
