import json

with open("primes.json") as file:
	primes = json.loads(file.read())

prime_set = set(primes)

def is_rotational(num):
	digits = list(str(num))
	for i in range(len(digits)-1):
		digits.append(digits.pop(0))
		if int("".join(digits)) not in prime_set:
			return False
	return True

count = 0
for p in primes:
	if p > 1000000:
		break
	if is_rotational(p):
		count += 1

print(count)