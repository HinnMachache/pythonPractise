# Program to check even or odd
"""digit = int(input("Enter a number: "))

if digit % 2 == 0:
    print("%d is even" % digit)
else:
    print("%d is odd" % digit)
"""

# Leap year calculate

"""year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.\n")
        else:
            print(f"{year} is not a leap year.\n")
    else:
        print(f"{year} is a leap year.\n")
else:
    print(f"{year} is not a leap year.\n")
"""

# Pizza Inn program
print("Welcome to Pizza inn\n")
bill = 0
size = input("Please input pizza size. (Small) (Medium) (Large): ").lower()

if size == "small":
    bill = 100
    print("Small pizza price is ksh. 100")
elif size == "medium":
    bill = 200
    print("Medium pizza price is ksh. 200")
else:
    bill = 300
    print("Large pizza price is ksh. 300")

add_Pepper = input("Add Pepper? (Y) or (N): ").lower()
if add_Pepper == "y":
    if size == "small":
        bill += 30
    else:
        bill += 50
cheese = input("Add Extra cheese? Choose(Y) or (N): ").lower()
if cheese == "y":
    bill = bill + 20

print(f"Total bill is {bill}")
print("Thank you for your order!")
