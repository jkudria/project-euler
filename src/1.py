result = 0
i = 1

while i <= 999:
	if i % 3 == 0 or i % 5 == 0:
		result = result + i
	i = i + 1

print(result)