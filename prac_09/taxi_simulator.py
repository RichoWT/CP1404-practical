from prac_09.car import Car
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive!")
    print(MENU)
    option = input(">>> ").lower()
    while option != "q":
        if option == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            print(taxi_choice)
        elif option == "d":
            print("2")
        else:
            print("invalid option")
        print(MENU)
        option = input(">>> ").lower()
    print("Thank you!")

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i+1} - {taxi}")

main()
