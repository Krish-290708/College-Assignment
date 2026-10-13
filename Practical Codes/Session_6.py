'''num = int(input("Enter a number: "))
original = num
total = 0
while num > 0:
    digit = num%10
    total += digit
    num //= 10
print(f"Sum of digits of {original} = {total}")'''

'''count = 1
while True:
    print(count)
    count += 1
    if not(count <= 10):
        break

count = 1
while count <= 10:
    count += 1
    print(count)'''


'''num = int(input("Enter a number:"))
count = 1
while True:
    print(f"{num} x {count} = {num*count} ")
    count += 1
    if not(count <= 10):
        break'''

'''secret = 7
while True:
    guess =  int(input("Guess the number "))'''

marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)


    
