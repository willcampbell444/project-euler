sums = {1: 0}

def sum_divisors(n):
	if n in sums:
		return sums[n]
	sum_divisors = 1
	square_root = n**(1/2)
	for i in range(2, int(square_root)+1):
		if n % i == 0:
			sum_divisors += i + n//i
	if n % square_root == 0:
		sum_divisors += square_root
	sums[n] = sum_divisors
	return sum_divisors

total = 0
for i in range(2, 10001):
	s = sum_divisors(i)
	if s != i and sum_divisors(s) == i:
		total += i

print(total)