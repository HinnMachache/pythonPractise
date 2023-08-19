# Working with strings
'''
name = input("What is your name? ")
print(f"Hello {name}")
'''

# Working with numbers
'''
num1, num2 = input("Input two numbers: ").split()
# Convert to Integers
num1 = int(num1)
num2 = int(num2)
# Sum
summ = num1 + num2
# Difference
difference = num1 - num2
# Product
product = num1 * num2
# Division
quotient = num1 / num2
# Result

print(f"{num1:d} + {num2:d} = {summ:d}")
print(f"{num1:d} - {num2:d} = {difference:d}")
print(f"{num1:d} * {num2:d} = {product:d}")
print(f"{num1:d} / {num2:d} = {quotient:f}")
'''

# Receive miles and convert to kilometres
# km = miles * 1.60934
# Ask user to input miles
'''
miles = input("Input miles: ")
# Convert to integers
miles = int(miles)
# Convert to Km
kilometres = miles * 1.60934
print(f"Kilometres = {kilometres:.2f}")
'''

# A simple calculator
# Choose an operator
'''
operator = input("Input an operator: ")
# Input numbers
num1, num2 = input("Input Numbers: ").split()
# Convert to int
num1 = int(num1)
num2 = int(num2)
# Calculator
if operator == "+":
    summ = num1 + num2
    print(f"{num1:d} + {num2:d} = {summ:d}")
elif operator == "-":
    diff = num1 - num2
    print(f"{num1:d} - {num2:d} = {diff:d}")
elif operator == "*":
    product = num1 * num2
    print(f"{num1:d} * {num2:d} = {product:d}")
elif operator == "/":
    quotient = num1 / num2
    print(f"{num1:d} - {num2:d} = {quotient:.2f}")
elif operator == "/":
    modulo = num1 % num2
    print(f"{num1:d} % {num2:d} = {modulo:.2f}")
else:
    print("Enter a valid operator")
'''

# if age is 5, Go to Kingergaten
# Ages 6 through 17 goes to grades 1 through 12
# if age is greater than 17 say go to college
# Complete with 10 or less lines

# Input age
age = eval(input("Input age: "))
# Conditions
if age < 5:
    print("Too young for school")
elif age == 5:
    print("Go to Kindergaten")
elif 6 <= age <= 17:
    grade = age - 5
    print(f"Go to grade {grade:d}")
else:
    print("Go to college")

