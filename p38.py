largest = -1

def is_pandigital(n):
	nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
	while n > 0 and n % 10 in nums:
		nums.remove(n % 10)
		n = n // 10
	return not bool(nums)

for num in range(1, 10000):
	s = ""
	count = 1
	while len(s) < 9:
		s += str(num*count)
		count += 1
	if len(s) == 9:
		n = int(s)
		if is_pandigital(n):
			if n > largest:
				largest = n

print(largest)