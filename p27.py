# fairly slow

import json
with open("primes.json") as file:
	primes = set(json.loads(file.read()))

largest = -1
p = 1

for a in range(-1000, 1001):
	for b in range(-1000, 1001):
		count = 0
		while count**2 + a*count + b in primes:
			count += 1
		if count > largest:
			largest = count
			p = a*b

print(p)