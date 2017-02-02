import json

with open("primes.json") as file:
	primes = json.loads(file.read())

def num_pfactors(n):
	i = 0
	num = 0
	while n > 1:
		if n % primes[i] == 0:
			num += 1
			while n % primes[i] == 0:
				n = n // primes[i]
		i += 1
	return num

n = 2
consec = 0

while consec < 4:
	if num_pfactors(n) == 4:
		consec += 1
	else:
		consec = 0
	n += 1

print(n-4)