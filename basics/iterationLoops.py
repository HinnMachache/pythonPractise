# FOR Loop
"""numbers = [2, 3, 4, 5, 10]
squares = []
for number in numbers:
    square = number ** 2
    squares.append(square)
print(squares)
"""

# FOR ... ELSE Loop
numbers = [2, 3, 4, 5, 10]
for number in numbers:
    print(number)
    """if number % 15 == 0:
        break
    else:
        print("Not even number.")
    """
else:
    print("Loop completed successfully!")