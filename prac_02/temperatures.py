"""
CP1404/CP5632 - Practical

"""


def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celcius_to_farenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = convert_farenheit_to_celcius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_farenheit_to_celcius():
    """convert farenheit to celcius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celcius_to_farenheit():
    """convert celcius to farenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
