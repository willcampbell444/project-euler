perimeters = {}

r = set(x**2 for x in range(1, 1000))

for x in range(1, 500):
	for y in range(x, 500):
		zz = (x**2 + y**2)
		if zz in r:
			zz = x+y+zz**(1/2)
			if zz in perimeters:
				perimeters[zz] += 1
			elif zz < 1000:
				perimeters[zz] = 1

l = -1
lp = -1
for key, val in perimeters.items():
	if val > l:
		l = val
		lp = key

print(lp, l)