"""CP1404 Practical """

"""Question 1."""
file = open("name.txt", "w")
name = input("Name: ")
print(name, file=file)
file.close()

"""Question 2."""
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hello {name}")

"""Question 3."""
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)

"""Question 4."""
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
