m = 100000

hexa = {n*(2*n-1) for n in range(1, m)}
pents = {n*(3*n-1)/2 for n in range(1, m)}

n = 286
while n < m:
	t = n*(n+1)/2
	if t in hexa and t in pents:
		print(t)
		break
	n = n + 1