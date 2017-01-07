# fairly slow

num = 600851475143

primes = []
pos = 2

largest = 0

while pos <= num:
	prime = True
	for p in primes:
		if pos % p == 0:
			prime = False
			break
	if prime:
		primes.append(pos)
		while num % pos == 0:
			num = num/pos
			largest = pos
	pos += 1

print(largest)