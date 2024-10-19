"""
CP1404 Practical
Hexadecimal Colours
"""

COLOUR_CODES = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "alice blue": "#f0f8ff", "alizarin crimson": "#e32636",
                "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiqueWhite": "#faebd7", "antiqueWhite1": "#ffefdb",
                "antiqueWhite2": "#eedfcc"}

colour_name = input("What is your colour name? ").lower()
while colour_name != "":
    print(f"The colour code for {colour_name} is {COLOUR_CODES[colour_name]}")
    colour_name = input("What is your colour name? ").lower()