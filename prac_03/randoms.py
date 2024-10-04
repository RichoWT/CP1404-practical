import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""1. 5 will be the smallest while 20 will be the largest"""

"""2. 3 will be the smallest while 9 will be the largest, and it wont be able to produce a 4"""

"""3. 2.5 will be smallest while 5.5 is the largest"""

print(random.randint(1, 100))