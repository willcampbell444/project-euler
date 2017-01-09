# calculating primes very slow
import json

with open("primes.json") as file:
	primes = json.loads(file.read())

total = 0
for i in primes:
	if i < 2000000:
		total += i
	else:
		break

print(total)