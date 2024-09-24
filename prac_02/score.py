"""
CP1404/CP5632 - Practical 2
"""
from random import randint


def main():
    result = get_valid_score("Enter score: ", 0, 100)
    print(determine_grade(result))
    print(f"The random grade is: {random_grade()}")


def get_valid_score(prompt, low, high):
    """get a valid score """
    score = float(input(prompt))
    while score < low or score > high:
        print("Invalid score")
        score = float(input(prompt))
    return score


def determine_grade(score):
    "sort the scores"
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"


def random_grade():
    """get random grade"""
    random_grade = randint(0, 100)
    determined_grade = determine_grade(random_grade)
    return determined_grade


main()
