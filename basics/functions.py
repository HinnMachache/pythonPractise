def hello(name="World"):
    print(f"Hello {name}")


def square(num):
    num_square = pow(num, 2)
    return num_square


def solve_forX(equation):
    # Split elements into variables
    x, add, num1, equals, num2 = equation.split()
    # Cast to int
    num1, num2 = int(num1), int(num2)
    # Print Results
    return "x = " + str(num2 - num1)


# print(solve_forX("x + 8 = 11"))


def fibonacci(num):
    """Print a fibonacci series up to num."""
    num1, num2 = 0, 1
    while num1 < num:
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2

    print()


def fibonacci_append(num):
    """Return a list of fibonacci series up to num."""
    fibonacci_list = []
    num1, num2 = 0, 1
    while num1 < num:
        fibonacci_list.append(num1)
        num1, num2 = num2, num1 + num2
    return fibonacci_list

    print()


"""
fibonacci_num = fibonacci_append(3)
print(fibonacci_num)
print(fibonacci(3))
"""

# Variable shadowing

x = 20  # Global Variable


def outerFunc():
    global x
    x = 30  # Variable shadowing
    y = 10  # Variable Shadowing
    print(x, y)

    def innerFunc():
        global x
        nonlocal y
        x = 10
        y = 49
        print(x, y)

    innerFunc()
    print(x , y)


outerFunc()
print(x)
