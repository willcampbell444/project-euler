
n = 1
oldn = 1
count = 2

while len(str(n)) < 1000:
	tmp = oldn
	oldn = n
	n += tmp
	count += 1

print(count)
