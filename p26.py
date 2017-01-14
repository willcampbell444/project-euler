import json

def period(b):
    x = 1
    while 10**x % b != 1:
        x += 1
    return x

with open("primes.json") as file:
    primes = json.loads(file.read())

def isRepeating(n):
    index = 0
    while primes[index] <= n:
        if primes[index] == 2 or primes[index] == 5:
            if n % primes[index] == 0:
                return False
            index += 1
            continue
        # if n % primes[index] == 0:
        #     return True
        index += 1
    return True

    return False

m = -1
o = 0

for n in range(2, 1001):
    if isRepeating(n):
        mOrder = period(n)
        if mOrder > m:
            m = mOrder
            o = n

print(o)