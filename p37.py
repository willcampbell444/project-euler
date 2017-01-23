import json, math

with open("primes.json") as file:
	primes = set(json.loads(file.read()))

def is_truncable(n):
	nn = n
	while n > 0:
		if n not in primes or nn not in primes:
			return False
		n = n // 10
		nn = nn % 10**int(math.log10(nn))
	return True

count = 0
total = 0
num = 10

while count < 11:
	if is_truncable(num):
		total += num
		count += 1
		print(count, num)
	num += 1

print(total)