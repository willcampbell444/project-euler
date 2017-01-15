values = [1, 2, 5, 10, 20, 50, 100, 200]

def ways_to_make(n):
	return coin_possibilities(n, 7)

def coin_possibilities(n, index):
	if index == 0:
		return 1
	return sum(coin_possibilities(i, index-1) for i in range(n, -1, -values[index]))

print(ways_to_make(200))