'''username = input("Enter your User ID: ")
password = input("Enter your Password: ")
if username == "krish@nmims":
    print("Valid Username")
else:
    print("Invalid")
if password.isdigit():
    print("Valid Password")

    sap_id = input("Enter your SAP ID:")
    roll_no = input("Enter your Roll no.:")
    course = input("Enter your Course name:")

    print("Student Information:")
    print(f"SAP ID: {sap_id}")
    print(f"Roll no.:{roll_no}")
    print(f"Course:{course}")
else:
    print("Invalid User ID or Password")'''

#Exercise
#1.
items = input("What is the item purchased:")
quantity = int(input("What is the quantity of the item purchased:"))
price = float(input("What is the price of the item:"))
total = price*quantity

print(f"{'items':<10}{'quantity':>10}{'price':>10}{'total':>10}")
print("-"*45)
print(f"{items:<10}{quantity:>10}{price:>10.2f}{total:>10.2f}")

#2.
'''num = int(input("Enter a number:"))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by either 3 or 5 or both.")'''
