"""Score Menu, Practical 2"""

def main():
    print("(G)et score | (P)rint result | (S)how stars | (Q)uit")
    option = input("Option: ").upper()
    while option != "Q":
        if option == "G":
            score = get_valid_score("Your score: ", 0, 100)
        elif option == "P":
            print(print_result(score))
        elif option == "S":
            print(print_stars(score))
        else:
            print("Invalid option")
        option = input("Option: ").upper()
    print("Farewell")


def get_valid_score(prompt, low, high):
    score = int(input(prompt))
    while score < low or score > high:
        print("invalid")
        score = int(input(prompt))
    return score


def print_result(score):
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


def print_stars(score):
    return "*" * score


main()
