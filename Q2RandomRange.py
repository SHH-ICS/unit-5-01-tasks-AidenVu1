import random

# ask the user for two numbers (1, 2, buckle my shoe is fire btw)
while True:
    try:
        a = float(input("Enter the first number bozo: "))
        b = float(input("Enter the second number bozo: "))
        break
    except ValueError:
        print("Ur bad!!! Please enter a valid input bozo!")

# make sure that a is less than b
if a > b:
    a, b = b, a

# random generator
random_number = random.uniform(a, b)

# print ur number
print("Random number between", a, "and", b, "is:", random_number)
