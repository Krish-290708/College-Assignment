'''1. 
for i in range(1, 6):
    print(i, "->", i ** 2)

2.
for i in range(0, 20, 5):
    print(i, end=" ")
print()
for i in range(10, 0, -2):
    print(i, end=" ")

3.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())
for ch in "Hi!":
    print(ch)

4.
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
print()'''

#EXERCISES
'''1.
for i in range(0, 50, 2):
    print(i, end=" ")

2.
for i in range(0, 11):
    print(7, "x", i, "=", 7*i)'''

3.
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    