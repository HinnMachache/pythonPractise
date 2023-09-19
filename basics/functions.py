def hello(name="World"):
    name = input("Enter name: ")
    print(f"Hello {name}")


def square(num):
    num_square = pow(num, 2)
    return num_square


num = int(input("Enter a number: "))
print(square(num))
name = input("Enter name: ")
hello(name)
