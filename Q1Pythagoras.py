import math
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

# ask for stuffs
while True:
    try:
        a = float(input("Enter the length of the first leg: "))
        b = float(input("Enter the length of the second leg: "))
        break
    except ValueError:
        print("No, Please enter a valid number.")

# mathing
c = math.sqrt(a**2 + b**2)

# roundin'
c = round(decimal.Decimal(str(c)), 2)

# hypotenoose
print("The length of the hypotenuse is: ", c)
