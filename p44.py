import math

# n3(3*n3 −1)/2 = n1(3*n1 −1)/2 + n2(3*n2 −1)/2
# n3(3*n3 −1) = n1(3*n1 −1) + n2(3*n2 −1)
# 3*n3*n3 − n3 = 3*n1*n1 − n1 + 3*n2*n2 − n2

# n4(3*n4 −1)/2 = n1(3*n1 −1)/2 - n2(3*n2 −1)/2
# n4(3*n4 −1) = n1(3*n1 −1) - n2(3*n2 −1)
# 3*n4*n4 − n4 = 3*n1*n1 − n1 - 3*n2*n2 − n2

# a + b = 3*n3*n3 − n3
# b = 3*n3*n3 − n3 - a
# a = 3*n3*n3 − n3 - b

# a - b = 3*n4*n4 − n4
# a - (3*n3*n3 − n3 - a) = 3*n4*n4 − n4
# 2a - 3*n3*n3 + n3 = 3*n4*n4 − n4
# 2a = 3*n4*n4 − n4 + 3*n3*n3 - n3
# 2a = d + c

# 3*n3*n3 − n3 - 2b = 3*n4*n4 − n4
# 2b = 3*n4*n4 − n4 - 3*n3*n3 + n3
# 2b = d - c
# c = d - 2b

pents = {n*(3*n-1)/2 for n in range(1, 10000)}

def is_penagonal(p):
	return p in pents

m = 10000

d = 5000000000

for a in range(1, m):
	ap = a*(3*a - 1)/2
	for b in range(a+1, m):
		bp = b*(3*b - 1)/2
		if bp - ap < d:
			if is_penagonal(bp - ap) and is_penagonal(bp + ap):
				d = bp - ap
print(d)