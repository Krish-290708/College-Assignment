#EXERCISE
#1.
item = input("what item/s have you bought?: ")
quantity = int(input("How many have you bought?: "))
price = float(input("What is the price of the item?: "))
total = price * quantity
print(f"Total = {total} ")

#2.
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5")
else:
    print(num, "is not divisible by both 3 and 5")