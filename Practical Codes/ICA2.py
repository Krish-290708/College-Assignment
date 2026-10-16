
#Q1. [Python Basics & Data Structures] Let marks = {"Maths": 85, "Stats": 90, "Python": 95}. 
# Print the keys, values and items separately, and then print the total of all the values. 

marks = {"Maths": 85, "Stats": 90, "Python": 95}

print("Keys:")
for key in marks:
    print(key)

print("\nValues:")
for value in marks.values():
    print(value)

print("\nItems:")
for key, value in marks.items():
    print(f"{key}: {value}")

print(f"\nTotal: {sum(marks.values())}")

# Q2. [Strings, I/O & Operators] Roll number 7 must be displayed as 007, and the number 10 must also be shown in binary. 
# Using f-string format specifiers (such as :03d and :b), print both results. 

roll_number = 7
binary_number = 10

print(f"Roll number: {roll_number:03d}") # :03d is used to format the number with leading zeros to make it 3 digits
print(f"Binary of 10: {binary_number:b}") # :b is used to format the number in binary representation

# Q3. [Control Flow & Loops] Accept an integer and print exactly one of: "Positive Even", "Positive Odd", "Negative" or 
#"Zero", using nested if statements. 

integer = int(input("Enter an integer: "))

if integer > 0:
    if integer % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if integer == 0:
        print("Zero")
    else:
        print("Negative")

# Q4. [Functions] Write a function grade(marks) that returns "A" (75 and above), "B" (60-74), "C" (40-59) or 
# "F" (below 40). Call it for the list [82, 67, 45, 30] using a loop and print each result.

def grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

marks_list = [82, 67, 45, 30]
for marks in marks_list:
    print(f"Grade for {marks} marks: {grade(marks)}")