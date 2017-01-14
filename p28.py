# count = 999*999
# summ = 0
# for i in range(4):
# 	count += 999
# 	summ += count

# print(summ)

def cornerSum(w):
	count = (w-2)*(w-2)
	summ = 0
	for i in range(4):
		count += (w-1)
		summ += count

	return summ

def diagSum(w):
	return 1 + sum(cornerSum(x) for x in range(3, w+1, 2))

print(diagSum(1001))