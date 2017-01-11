days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1
sundays = 0

for _ in range(100):
	for month in month_lengths:
		if (day+1) % 7 == 0:
			sundays += 1
		day += month

print(sundays)