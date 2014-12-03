number_to_factorize = int(input("Number: "))

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
p = 0

while len(primes) != (number_to_factorize / 2):
	if check_prime(p) == True:
		primes.append(p)
	p += 1

factors = []

def factorization(x):

	for n in primes:
		while x % n == 0:
			x = x/n
			factors.append(n)
			pass


factorization(number_to_factorize)
print(factors[-1])