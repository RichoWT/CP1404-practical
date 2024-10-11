numbers = []
for i in range(1, 6):
    number = int(input("Number: "))
    numbers.append(number)
print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average = sum(numbers) / len(numbers)
print(f"The average of the numbers {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input('What is your username? ')
while name not in usernames:
    print("Access Denied")
    name = input('What is your username? ')
print("Access Granted")