
import random

NUMBER_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_picks = int(input("How many quick picks ? "))
    while quick_picks <= MINIMUM:
        print("Invalid Value")
        quick_picks = int(input("How many quick picks ? "))

    for i in range(quick_picks):
        picks = []
        for j in range(NUMBER_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in picks:
                number = random.randint(MINIMUM, MAXIMUM)
main()
