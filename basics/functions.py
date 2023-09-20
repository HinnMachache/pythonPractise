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
    print("-- This parrot wouldn't", action, end=" ")   # Keyword argument to print()
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()


parrot(1000)
parrot(voltage=1000)    # Keyword Arguments
parrot(voltage=10000, action="VOOOOOM") # 2 Keyword Arguments
parrot(action="VOOOOM", voltage=10000)  # 2 Keyword Arguments
parrot("a million", "bereft of life", "jump")   # 3 Positional Arguments
parrot("a thousand", state="Pushing up the daises") # 1 Positional Argument and 1 Keyword Argument
