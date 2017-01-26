# def d(x):
# 	n = 1
# 	_x = x
# 	prev = 0
# 	while n*(10**n - 10**(n-1)) <= x:
# 		n += 1
# 	n -= 1
# 	x = int(x - n*(10**n - 10**(n-1)))
# 	# print(_x, x, n)
	
# 	z = 10**(n)

# 	# # print(n)
# 	if n == 0:
# 		z = 0

# 	l = 0
# 	while l <= x:
# 		l += n+1
# 		z += 1
# 	l -= n+1
# 	z -= 1
# 	print(z, x, l, prev)
# 	return int(str(z)[x-l])
# 	# print("Hi:", x_, x, n*10**n, prev)
# 	# print(str(z)[x-l], x, l, n)
# # print(d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))
# # print(d(1), d(10), d(100), d(1000), d(10000), d(100000), d(1000000))
# for i in range(1, 300):
# 	print(i, d(i))

# # print(d(190), d(191), d(192), d(193))
product = 1
to_print = [1, 10, 100, 1000, 10000, 100000, 1000000]
count = 0
n = 0
while to_print:
	current = to_print.pop(0)
	while count <= current:
		count += len(str(n))
		n += 1
	product *= int(str(n-1)[current-(count-len(str(n-1)))])
print(product)