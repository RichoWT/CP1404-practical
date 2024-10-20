"""
CP1404 Practical
Email to name dictionary
"""


def main():
    """Verify the name and ask for the name """
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        verification = input(f"Is your name {name}? Y/N: ")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Take name from email"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
