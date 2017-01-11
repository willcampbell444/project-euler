import json

with open("names.txt") as file:
	names = json.loads(file.read())

names.sort()

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for i in range(len(names)):
	total += (sum(characters.index(j)+1 for j in names[i]))*(i+1)

print(total)