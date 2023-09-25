import math


def hello(name="World"):
    print(f"Hello {name}")


def square(num):
    num_square = pow(num, 2)
    return num_square


# Lambda expression
find_square = lambda num: num ** 2


# print(find_square(5))

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

'''
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

'''


# Defining a function with a variable number of arguments

def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        ok = ok.lower()
        if ok in ('y', 'ye', 'yes'):
            print("We're glad!")
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            print("Ooops! We're working on it.")
            return False
        retries -= 1
        if retries <= 0:
            raise ValueError("invalid user response!")
        print(reminder)


# ask_ok("Are you okay? ", reminder="Come on Think", retries=5)

def input_pin(prompt, retries=3, reminder="Incorrect pin"):
    while True:
        pin = int(input(prompt))
        if pin == 2022:
            return True
        retries -= 1
        if retries <= 0:
            raise ValueError("Pin Blocked. Input PUK")
        print(reminder)


# input_pin("Input sim pin: ")


def parrot(voltage, state="stiff", action="Voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")  # Keyword argument to print()
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()


"""
parrot(1000)
parrot(voltage=1000)  # Keyword Arguments
parrot(voltage=10000, action="VOOOOOM")  # 2 Keyword Arguments
parrot(action="VOOOOM", voltage=10000)  # 2 Keyword Arguments
parrot("a million", "bereft of life", "jump")  # 3 Positional Arguments
parrot("a thousand", state="Pushing up the daises")  # 1 Positional Argument and 1 Keyword Argument

# Keyword Argument must follow positional arguments
parrot()  # required argument missing, error
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument, incorre
parrot(110, voltage=220)  # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

"""


def sum_All(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


# print(sum_All(5, 5, 5, 5, 5))


def sumOfAll(**kwargs):
    wordList = []
    for word in kwargs:
        wordList.append(kwargs[word])
    return wordList


# print(sumOfAll(num="5", num1="4", num2="3", num3="2", num4="1"))


def cheeseshop(kind, *args, **kwargs):
    print(f"-- Do you have any {kind}?")
    print("-- I'm sorry, we're all out of {:s}".format(kind))
    for arg in args:
        print(arg)
    print("--" * 40)
    for kwarg in kwargs:
        print(kwarg, ":", kwargs[kwarg])


'''cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
'''


# Lambda Functions == Anonymous functions(Functions with no names, Function body is an expression)
def sum_equations(num):
    return (3 * num) + 1  # Equation == 3x + 1


print(sum_equations(4))

# Lambda Equivalent
equation = lambda num: (3 * num) + 1

# print(equation(4))

# Lambda expression to sort name list according to last name

employees = ["James Ichungwa", "Ruto Musalia Kaiser", "Dan Owiti", "Mohammed Ali", "James Bond", "David Guetta",
             "Da Avinci", "Malcom King X", "Abel Mackonnen Tesfaye"]

employees.sort(key=lambda employees: employees.split(" ")[-1].lower())


# print(employees)


def rectangle_area():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    area = length * width
    print("Rectangle area: ", area)


def square_area():
    width = float(input("Enter Width: "))
    area = width * width
    print(f"Square area: {area}")


def circle_area():
    radius = float(input("Enter radius: "))
    area = math.pi * (math.pow(radius, 2))
    print("Circle area: {:.2f}".format(area))


def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "square":
        square_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Available shapes are: Circle, Square and Rectangle. \n Try Again.")


def main():
    shape_type = input("Get Area of What shape: ")
    get_area(shape_type)


# main()
'''for meow in range(3):
    print("Meow!")
'''

while True:
    num = int(input("Enter a number: "))
    if num > 0:
        break
