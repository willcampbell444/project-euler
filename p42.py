import json, string

with open("words.txt") as file:
	words = json.loads(file.read())

triangles = {0.5*i*(i+1) for i in range(1, 1000)}

def sumletter(word):
	return sum(string.ascii_uppercase.index(char)+1 for char in word)

count = 0
for word in words:
	if sumletter(word) in triangles:
		count += 1

print(count)