"""
CP1404
time started: 5:10pm (estimate - 1 day)

"""

from prac_07.project import Project
import datetime

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = get_data(FILENAME)
    print(f"5 places loaded from {FILENAME}")
    print(
        "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit ")
    option = input(">>> ").upper()
    while option != "Q":

        if option == "L":
            print("Projects loaded.")

        elif option == "S":
            print("test2")

        elif option == "D":
            completed_projects = []
            incomplete_projects = []
            for project in projects:
                if project.is_complete():
                    completed_projects.append(project)
                else:
                    incomplete_projects.append(project)
            print("Incomplete projects:")
            for project in incomplete_projects:
                print(project)
            print("\nCompleted projects:")
            for project in completed_projects:
                print(project)

        elif option == "F":
            print("test4")

        elif option == "A":
            print("test5")

        elif option == "U":
            i = 1
            for project in projects:
                print(f"{i}. {project}")
                i += 1
            choice = get_valid_choice(projects)
            print(projects[choice - 1])

        else:
            print("invalid option")
        print(
            "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit ")
        option = input(">>> ").upper()
    print("Thank you!")


def get_data(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        return projects


def get_valid_choice(projects):
    try:
        choice = int(input("Project choice: "))
        if choice < 0 or choice > len(projects):
            print(f"Project choice must be between 1 and {len(projects)}")
            return get_valid_choice(projects)
        else:
            return choice
    except ValueError:
        print("Invalid input")
        return get_valid_choice(projects)


def get_valid_percentage():
    try:
        percentage = int(input("Enter completion percentage (0-100): "))
        if percentage < 0 or percentage > 100:
            print("Completion percentage must be between 0 and 100.")
            return get_valid_percentage()
        else:
            return percentage
    except ValueError:
        print("Invalid input")
        return get_valid_percentage()


main()
