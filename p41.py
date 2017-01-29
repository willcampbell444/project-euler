import json, math

with open("primes.json") as file:
	primes = json.loads(file.read())

def is_pan(n):
	digs = {i for i in range(1, len(str(n))+1)}
	while n > 0:
		if n % 10 in digs:
			digs.remove(n % 10)
			n = n // 10
		else:
			return False
	return not digs

for p in reversed(primes):
	if is_pan(p):
		print(p)
		break

count = primes[-1]

threshhold = 1000000000

try:
	while count < threshhold:
		count += 2
		if count % 10000001 == 0:
			print(count/1000000000)
		root = math.sqrt(count)
		prime = True
		for p in primes:
			if p > root:
				break
			if count % p == 0:
				prime = False
				break
		if prime:
			primes.append(count)
except:
	pass

print(primes[-1])

with open("primes.json", "w") as file:
	file.write(json.dumps(primes))