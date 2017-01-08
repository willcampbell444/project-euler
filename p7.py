import json

primes = []

count = 2
while len(primes) < 10001:
	count += 1
	isPrime = True
	for p in primes:
		if count % p == 0:
			isPrime = False
			break
	if isPrime:
		primes.append(count)

print(primes[-1])

with open("primes.json", "w") as file:
	file.write(json.dumps(primes))