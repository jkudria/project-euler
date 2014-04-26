result = 0
i2 = 1
i = 1

while i2 in range(1, 4000000) and i in range(1, 4000000):

	i = i + i2
	i2 = i + i2

	if i % 2 == 0:
		result += i

	if i2 % 2 == 0:
		result += i2

	print(i)
	print(i2)


print()
print(result)