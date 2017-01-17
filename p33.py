
for top in range(10, 100):
	for bottom in range(10, 100):
		if top < bottom and top % 10 != 0 and bottom % 10 != 0:
			if top % 10 == bottom % 10:
				if top/bottom == (top//10)/(bottom//10):
					print(top, bottom)
			elif top % 10 == bottom // 10:
				if top/bottom == (top//10)/(bottom%10):
					print(top, bottom)
			elif top // 10 == bottom % 10:
				if top/bottom == (top%10)/(bottom//10):
					print(top, bottom)
			elif top // 10 == bottom // 10:
				if top/bottom == (top%10)/(bottom%10):
					print(top, bottom)