PASSWORD_LENGTH = 10

password = input("Enter password: ")
while len(password) < PASSWORD_LENGTH:
    password = input("Enter password: ")

print("*" * len(password))