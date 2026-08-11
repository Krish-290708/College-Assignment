#1. [Data Types & Operators] Write a program to convert a Celsius temperature to Fahrenheit and round 
#the result to the nearest whole number using round(); test it with an input that rounds DOWN and
#one that rounds UP.

'''celsius = float(input("Enter the temperature in Celsius:"))
fahrenheit = (celsius * 9/5) +32
print("Temperature in fahrenheit:", round(fahrenheit))'''

#2. [Strings] Write a program to check if a sentence STARTS WITH the word "Python" and ENDS WITH a 
#full stop ".", using startswith() and endswith().

sentence = input("Enter the sentence: ")
if sentence.lower().startswith("python") and sentence.endswith("."):
    print("The sentence starts with Python and ends with a full stop.")
else:
    print("The condition is not satisfied.")

#3.[Lists & Tuples] Let empty_list = []. Print bool(empty_list); then append one item to it and
#print bool(empty_list) again — add a comment on what this shows about empty vs non-empty lists.

'''empty_list = []
print(bool(empty_list))
empty_list.append("Python")
print(bool(empty_list))
#This shows that an empty list is false, while a non-empty list is true.'''

#4.[Sets & Dictionaries] Marks for 5 subjects are stored in a dictionary as {subject: marks}. 
#Write a program to find and print the subject with the HIGHEST marks.

'''marks = {
    "Math":96,
    "Physics":92,
    "Chemistry":88,
    "English":95,
    "Computer Science":97
}
highest_subject = max(marks,key=marks.get)
print("Subject with highest marks:", highest_subject)
print("Marks:", marks[highest_subject])'''


