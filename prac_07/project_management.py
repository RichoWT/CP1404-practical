"""
CP1404
time started: 5:10pm (estimate - 1 day) ( 9 Nov )
time finished: 11:46pm ( 10 Nov )
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
            save_project(projects)
            print(f"Projects saved to {FILENAME}")

        elif option == "D":
            sort_project(projects)
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
            filter_date_str = get_valid_date()
            filter_date = datetime.datetime.strptime(filter_date_str, "%d/%m/%Y").date()
            filtered_projects = filter_project_with_date(projects, filter_date)
            for project in filtered_projects:
                print(f"{project}")

        elif option == "A":
            print("Let's add a new project")
            name = get_valid_name()
            new_date = get_valid_date()
            priority = get_valid_priority()
            cost_estimate = get_valid_cost_estimate()
            completion_percentage = get_valid_percentage()
            new_project = Project(name, new_date, priority, cost_estimate, completion_percentage)
            projects.append(new_project)
            sort_project(projects)

        elif option == "U":
            i = 1
            for project in projects:
                print(f"{i}. {project}")
                i += 1
            choice = get_valid_choice(projects)
            selected_project = projects[choice - 1]
            new_percentage = get_valid_percentage()
            selected_project.completion_percentage = new_percentage

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


def get_valid_name():
    name = input("Name: ")
    if name != "":
        return name
    print("name cannot be blank.")
    return get_valid_name()


def get_valid_date():
    new_date = input("start date (dd/mm/yyyy): ")
    try:
        datetime.datetime.strptime(new_date, "%d/%m/%Y")
        return new_date
    except ValueError:
        print("Invalid date format")
        return get_valid_date()


def get_valid_priority():
    try:
        priority = int(input("Priority: "))
        if priority > 0:
            return priority
        else:
            print("Priority must be more than 0.")
            return get_valid_priority()
    except ValueError:
        print("Invalid input, please enter a real number")
        return get_valid_priority()


def get_valid_cost_estimate():
    try:
        cost_estimate = float(input("Cost estimate: "))
        if cost_estimate >= 0:
            return cost_estimate
        else:
            print("Cost cannot be less than 0")
            return get_valid_cost_estimate()
    except ValueError:
        print("Invalid input, please enter a real number")
        return get_valid_cost_estimate()


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


def sort_project(projects):
    return projects.sort(key=lambda project: project.priority)


def filter_project_with_date(projects, filter_date):
    filtered_projects = []
    for project in projects:
        if project.start_date >= filter_date:
            filtered_projects.append(project)
    return filtered_projects


def save_project(projects):
    with open(FILENAME, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


main()
