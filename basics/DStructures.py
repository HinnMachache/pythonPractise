# Lists
'''
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[:-3])
print(numbers[-3:])
numbers2 = [6, 7, 8, 9]
print((numbers + numbers2))
numbers[4] = 4
print(numbers)
numbers.append(numbers2)
print(numbers)
print(len(numbers))
numbers[5] = 0
print(numbers)
'''


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.index('apple', 0))
del fruits[0:-3]
print(fruits)