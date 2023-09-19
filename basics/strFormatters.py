'''
# str.format()
str1 = "This is a {:d} string {}"

print("my name is {:s}, I'm enrolled in {:s} , and it's {:s}".format("Benny", "ALX Program", "very hard"))
print("my name is {1:s}, I'm enrolled in {0:s} , and it's {2:s}".format("Benny", "ALX Program", "very hard"))
print("my name is {1:s}, I'm enrolled in {2:s} , and it's {0:s}".format("Benny", "ALX Program", "very hard"))
print(str1.format(5,"example"))
'''

# Str Methods
name = input("What is your name? ")
# Remove whitespace and Capitalize
name = name.strip().title()
print(name)
