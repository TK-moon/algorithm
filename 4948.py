import math

def isPrime(num):
	if num == 1: return False
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0: return False
	return True;

primeList = []

for i in range(2, 123456 * 2):
	if isPrime(i): primeList.append(i)

while True:
	n = int(input())
	if n == 0: break
	
	count = 0
	for i in primeList:
		if n < i <= n * 2: count += 1
	print(count)