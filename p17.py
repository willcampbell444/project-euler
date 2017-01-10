words = [
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen"
]

prefixes = [
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety"
]

def intToWord(num):
	if num < 20:
		return words[num]
	elif num < 100:
		second = num % 10
		first = num // 10
		if second == 0:
			return prefixes[first-2]
		return prefixes[first-2]+" "+words[second]
	elif num < 1000:
		second = num % 100
		first = num // 100
		if second == 0:
			return words[first] + " hundred"
		return words[first] + " hundred and " + intToWord(second)
	elif num == 1000:
		return "one thousand"


total = 0

for n in range(1, 1001):
	total += sum(len(i) for i in intToWord(n).split(" "))
	print(n, intToWord(n), sum(len(i) for i in intToWord(n).split(" ")))

print(total)