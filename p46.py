import json

with open("primes.json") as file:
	primes = set(json.loads(file.read()))

n = 1
done = False
while not done:
	n += 2
	if n not in primes:
		s = 1
		ssq = 2
		success = False
		while ssq < n:
			if (n - ssq) in primes:
				success = True
				break
			s += 1
			ssq = 2*s**2
		if not success:
			done = True

print(n)