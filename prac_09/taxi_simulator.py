from prac_09.car import Car
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's Drive!")
    print(MENU)
    option = input(">>> ")
    while option != "q":
        if option == "c":
            print("1")
        elif option == "d":
            print("2")
        else:
            print("invalid option")
        print(MENU)
        option = input(">>> ")
    print("Thank you!")


main()
