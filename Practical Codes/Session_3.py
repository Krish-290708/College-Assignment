#EXERCISE
#1.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)
if common:
    print("Common elements are:", common)
else:
    print("No common elements")

#2.
students = {
    "Aman": 85,
    "Rahul": 92,
    "Krish": 96,
    "Priya": 88,
    "Anjali": 91
}

topper = ""
highest = 0

for student in students:
    if students[student] > highest:
        highest = students[student]
        topper = student

print("Topper:", topper)
print("Marks:", highest)