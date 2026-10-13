1.
'''numbers = [4, 8, 15, 16, 23, 42]
target = 16
for n in numbers:
    if n == target:
        print("Found", target)
        break
    print("Checked", n)

2. 
for i in range(1, 11):
    if i % 2 == 0:
        continue         # skip even numbers
    print(i, end=" ")

3.
for i in range(1, 6):
    if i == 3:
        pass      # nothing happens, placeholder for future code
    print(i)'''

'''4. 
correct_password = "python123"
for attempt in range(1, 4):
    entered = input(f"Attempt {attempt}: Enter password: ")
    if entered == correct_password:
        print("Access granted!")
        break
else:
    print("Access denied -- too many attempts")'''

#EXERCISES
1.
'''for i in range(1,50):
    print(i, end=" ")
    if i % 5 == 0 and i % 7 == 0:
        break'''

2. 
for i in range(1, 30):
    if i % 3 == 0:
        continue
    print(i, end=" ")
    

 