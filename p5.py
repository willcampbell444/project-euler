factors = {}

primes = []

for n in range(2, 21):
	isPrime = True
	for p in primes:
		if n % p == 0:
			isPrime = False
			break
	if isPrime:
		primes.append(n)
	for p in primes:
		power = 0
		while n % p == 0:
			n = n/p
			power += 1
		if p not in factors:
			factors[p] = power
		elif power > factors[p]:
			factors[p] = power

total = 1
for base, power in factors.items():
	total = total * base**power

print(total)