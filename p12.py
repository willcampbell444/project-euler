num_divisors = 1
num = 1
count = 1
l = -1

while num_divisors < 500:
	count += 1
	num += count
	num_divisors = 2
	for i in range(2, int(num**(1/2))+1):
		if num % i == 0:
			num_divisors += 2
	if num_divisors > l:
		l = num_divisors
		print(l, num)

print(num)