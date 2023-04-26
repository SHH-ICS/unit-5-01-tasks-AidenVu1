import random

# Generate 2 random numbers between 1 and 100
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# the question itself
answer = int(input("What is " + str(num1) + " + " + str(num2) + "? "))

# Check if the user's answer is correct (and bully them is they get it wrong)
if answer == num1 + num2:
    print("Correct, you are smarter than a 1st grader!")
else:
    print("You are correct! If you were an idiot, try again bozo you're wrong, answer is:", num1 + num2)