#EXERCISE
#1.
numbers = [12, 45, 7, 89, 23, 56]
largest = numbers[0]
smallest = numbers[0]

for num in numbers: #num is the loop variable
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)

#2.
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("List after swapping:", numbers)

#3.
subjects = ("Maths", "Physics", "Chemistry", "English", "Computer Science")
for subject in subjects: #subject is the loop variable here
    print(subject)

