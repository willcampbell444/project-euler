powers = {
	0: 0,
	1: 1,
	2: 32,
	3: 243,
	4: 1024,
	5: 3125,
	6: 7776,
	7: 16807,
	8: 32768,
	9: 59049
}

grandTotal = 0

for n in range(2, 1000000):
	total = 0
	tmpnum = n
	while total <= n and tmpnum > 0:
		total += powers[tmpnum % 10]
		tmpnum = tmpnum // 10
	if total == n:
		grandTotal += total

print("total", grandTotal)