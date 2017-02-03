import json

with open("primes.json") as file:
	allprimes = json.loads(file.read())

primes = [i for i in allprimes if i > 999 and i < 10000]

prime_set = set(primes)

print(len(primes))

def isPerm(n, m):
	return {i for i in str(n)} == {i for i in str(m)}

for n1 in range(len(primes)):
	p1 = primes[n1]
	for n2 in range(n1+1, len(primes)):
		p2 = primes[n2]
		if p2 + p2 - p1 > 9999:
			break
		if (p2 + p2 - p1 in prime_set) and isPerm(p1, p2) and isPerm(p1, p2 + p2 - p1):
			print(p1, p2, p2 + p2 - p1)