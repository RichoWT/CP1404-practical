"""
CP1404/CP5632 - Practical
"""


def main():
    result = get_valid_score("Enter score: ", 0, 100)
    print(determine_grade(result))


def get_valid_score(prompt, low, high):
    score = float(input(prompt))
    while score < low or score > high:
        print("Invalid score")
        score = float(input(prompt))
    return score


def determine_grade(score):
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


main()
