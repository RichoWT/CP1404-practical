FILENAME = "wimbledon.csv"
COUNTRY = 1
CHAMPION = 2


def main():
    """Read data file and print details.."""
    records = get_records(FILENAME)
    champion_and_count, countries = process_records(records)
    display_results(champion_and_count, countries)


def process_records(records):
    """create dictionary and country from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY])
        try:
            champion_to_count[record[CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    """Get records from file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            fragment = line.strip().split(",")
            records.append(fragment)
    return records


main()