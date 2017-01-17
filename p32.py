
nums = "123456789"
digits = [(1, 4, 4), (2, 3, 4)]

def perm(stuff, length):
	if length == 1:
		return [char for char in stuff]
	perms = []
	for i in range(len(stuff)):
		perms.extend(stuff[i] + j for j in perm(stuff[:i]+stuff[i+1:], length-1))
	return perms

products = set()

for d in digits:
	for a in perm(nums, d[0]):
		unused_nums = list(nums)
		for char in a:
			unused_nums.remove(char)
		for b in perm("".join(unused_nums), d[1]):
			if a != b:
				unused_nums2 = unused_nums[:]
				for char in b:
					unused_nums2.remove(char)
				result = int(a)*int(b)
				success = True
				for char in str(result):
					if char in unused_nums2:
						unused_nums2.remove(char)
					else:
						success = False
						break
				if success and len(unused_nums2) == 0:
					products.add(result)

print(sum(products))