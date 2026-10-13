#1: Call by Value behaviour (immutable arguments)

def try_to_change(n):
    n = n + 100
    return n

x = 5
result = try_to_change(x)
print("Original x:", x)
print("Returned result:", result)

#2: Call by Reference behaviour (mutable arguments)

def add_item(my_list):
    my_list.append("new item")

items = ["pen", "book"]
add_item(items)
print(items) # original list WAS modified

#33: Returning multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = get_min_max([4, 8, 1, 9, 3])
print("Lowest:", lowest, "Highest:", highest)

#4: A recursive function using return (factorial)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#Exercises
#1. Write a function that takes a list of prices and applies a 10% discount to each price IN PLACE (modifying
#the original list).

def apply_discount(prices):
    for i in range(len(prices)):
        prices[i] *= 0.9  # Apply 10% discount

items_prices = [100, 200, 300]
apply_discount(items_prices)
print(items_prices)

#2. Write a recursive function to compute the sum of the first n natural numbers.
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

print(sum_natural(5))