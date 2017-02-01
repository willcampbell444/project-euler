def perm(data):
	if len(data) == 1:
		return [data]
	perms = []
	for x in range(len(data)):
		for i in perm(data[:x]+data[x+1:]):
			perms.append([data[x]] + i)
	return perms

divs = [2, 3, 5, 7, 11, 13, 17]

total = 0

for p in perm(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
	strp = "".join(p)
	success = True
	for x in range(len(divs)):
		if int(strp[x+1:x+4]) % divs[x] != 0:
			success = False
			break
	if success:
		total += int(strp)

print(total)