def main():
    # print_column(3)
    # print_row(3)
    print_square(4)


def print_column(height):
    print("#\n" * height, end="")


def print_row(width):
    print("?" * width)


def print_square(size):
    # For each row
    for i in range(size):
        # For each column
        for j in range(size):
            # Print Brick
            print("#", end="")
        print()


main()
