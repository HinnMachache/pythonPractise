def fibo():
	a , b = 0, 1
	while a < 100:
		print(a, end = ' ')
		a , b = b , a + b
	print()
	
def fibo2():
	result = []
	a, b = 0, 1
	while a < 100:
		result.append(a)
		a, b = a, a + b
	return result

