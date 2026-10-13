#1: Defining and calling a simple function

import numbers
from unicodedata import name


def calculate_area(length, breadth):
    return length * breadth

print(calculate_area(5, 3))
print(calculate_area(10, 2))

#2: Default parameters and keyword arguments

def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Rhea")
greet("Kabir", "Welcome")
greet(greeting="Hi", name="Zoya")

#3: Variable-length arguments using *args

def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))

#4: Scope of a function -- local vs global

x = 10 # global variable

def show_value():
    y = 5 # local variable
    print("Inside function:", x, y)

show_value()
print("Outside function:", x)
#print(y) # This would raise NameError -- y only exists inside the function

#Exercises
#1. Write a function is_prime(n) that returns True or False.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # The loop checks for factors from 2 to the square root of n because if n has a factor larger than its square root, it must also have a factor smaller than its square root.
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
print(is_prime(10)) # False

#2. Write a function that accepts any number of arguments and returns their average using *args.
def calculate_average(*numbers):
    if not numbers:                 # If no arguments are provided, return 0
        return 0
    return sum(numbers) / len(numbers)

print(calculate_average(1, 2, 3))      # 2.0
print(calculate_average(10, 20, 30, 40))  # 25.0
print(calculate_average())              # 0