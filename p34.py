import math

digits = 1

factorials = [0]+[math.factorial(i) for i in range(1, 10)]

def sumFactorial(num):
	total = 0
	while num > 0:
		total += math.factorial(num % 10)
		num = num // 10

	return total


while int("9"*digits) < math.factorial(9)*digits:
	digits += 1

print(digits)

total = 0
for n in range(3, 10000000):
	if n == sumFactorial(n):
		total += n

print(total)