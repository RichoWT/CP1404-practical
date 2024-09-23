PASSWORD_LENGTH = 10


def main():
    password = get_password(PASSWORD_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password(PASSWORD_LENGTH):
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH:
        password = input("Enter password: ")
    return password


main()
