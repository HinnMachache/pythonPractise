import random

print("--------------------------Toss a coin----------------------------")
choice = input("Choose a side (Head) or (Tail): ").lower()
option: int

if choice == "head":
    option = 1
elif choice == "tail":
    option = 0
else:
    print("Wrong choice! Try again.")
side = random.randint(0, 1)

if side == 1:
    print("Side of coin: Head")
else:
    print("Side of coin: Tail")

if side == option:
    print("Congratulations! You win!")
else:
    print("Oops! try again!")
