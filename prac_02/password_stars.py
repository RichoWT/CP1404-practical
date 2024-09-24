"""
CP1404/CP5632 - Practical 2
"""

PASSWORD_LENGTH = 10


def main():
    password = get_password(PASSWORD_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    """multiply stars with the length of the password"""
    print("*" * len(password))


def get_password(PASSWORD_LENGTH):
    """get valid password"""
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH:
        password = input("Enter password: ")
    return password


main()
