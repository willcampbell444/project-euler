import math

def perm(digits, n):
	if len(digits) == 1:
		return digits
	pos = 0
	factorial = math.factorial(len(digits)-1)
	while factorial*(pos+1) < n:
		pos += 1
	return digits[pos] + perm(digits[:pos] + digits[pos+1:], n - factorial*pos)

print(perm("0123456789", 1000000))