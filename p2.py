total = 0

current = 1
previous = 1

while current < 4000000:
	if current % 2 == 0:
		total += current
	current += previous
	previous = current - previous

print(total)