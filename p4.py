import math

def isPalindrome(string):
	return string[:len(string)//2] == string[math.ceil(len(string)/2):][::-1]


largest = -1

for n1 in reversed(range(1, 999)):
	for n2 in reversed(range(1, 999)):
		product = n1*n2
		if product > largest:
			if isPalindrome(str(product)):
				largest = product

print(largest)
