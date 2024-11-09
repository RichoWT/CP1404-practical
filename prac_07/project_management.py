"""
CP1404
time started: 5:10pm (estimate - 1 day)

"""


FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    print(f"5 places loaded from {FILENAME}")
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit ")
    option = input(">>> ").upper()
    while option != "Q":
        if option == "L":
            print("Test1")
        elif option == "S":
            print("test2")
        elif option == "D":
            print("test3")
        elif option == "F":
            print("test4")
        elif option == "A":
            print("test5")
        elif option == "U":
            print("test6")
        else:
            print("invalid option")




main()
