import json

with open("primes.json") as file:
	allprimes = json.loads(file.read())

primes = [i for i in allprimes if i < 1000000]
prime_set = set(primes)

maxlen = -1
mprime = -1

for start in range(5):
	length = 0
	summ = 0
	for p in primes[start:]:
		summ += p 
		length += 1
		if summ in prime_set and length > maxlen:
			maxlen = length
			mprime = summ

print(mprime, maxlen)