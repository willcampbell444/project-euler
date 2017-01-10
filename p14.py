lengths = {1: 1}

def lenChain(n):
	if n in lengths:
		return lengths[n]
	else:
		num = n
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3*num + 1
		length = 1 + lenChain(num)
		lengths[n] = length
		return length

largest = -1
n = -1
for i in range(2, 1000001):
	length = lenChain(i)
	if length > largest:
		largest = length
		n = i

print(n)