# Imports
import math
import random

# Collecting Data
num_1 = int(input("Pick your First Number: "))
num_2 = int(input("Pick your second Number: "))
operator = input("Pick your Operator: ")


# Function
def Numbers(num_1, num_2):
    if operator == "+":
        print(num_1 + num_2)

    elif operator == "-":
        print(num_1 - num_2)

    elif operator == "*":
        print(num_1 * num_2)

    elif operator == "/":
        print(num_1 / num_2)


Numbers(num_1, num_2)
