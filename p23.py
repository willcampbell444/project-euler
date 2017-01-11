import math

sums = {1: 0}

def sum_divisors(n):
	if n in sums:
		return sums[n]
	sum_divisors = 1
	square_root = n**(1/2)
	for i in range(2, math.ceil(square_root)):
		if n % i == 0:
			sum_divisors += i + n//i
	if n % square_root == 0:
		sum_divisors += square_root
	sums[n] = sum_divisors
	return sum_divisors

abundant = []

for i in range(2, 28124):
	s = sum_divisors(i)
	if s > i:
		abundant.append(i)

notSums = set(i for i in range(2, 28124))

for i in abundant:
	for j in abundant:
		notSums.discard(i+j)

total = 1+sum(notSums)

print(total)