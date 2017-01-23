def is_palindrome_10(n):
	s = str(n)
	return s == s[::-1]

def is_palindrome_2(n):
	l = []
	while n > 0:
		l.append(n % 2)
		n = n // 2
	return l == l[::-1]

total = 0
for num in range(1, 1000000):
	if is_palindrome_10(num) and is_palindrome_2(num):
		total += num

print(total)