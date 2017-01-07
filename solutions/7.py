def check_prime(x):
	if x < 2 or (x % 2 == 0 and x != 2):
		return False

	if x == 2:
		return True

	for n in range(2, int(x ** 0.5) + 1):
		if x % n == 0:
			return False

	return True

primes = []
x = 0

while len(primes) != 10001:
	if check_prime(x) == True:
		primes.append(x)
	x += 1

answer = primes[10000]
print(answer)