#EXERCISE
#1.
text = input("Enter a string: ")
count = 0

for letter in text:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        count = count + 1
print("Number of vowels:", count)

#2.
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = string1 + " " + string2
print("Concatenated string:", result)