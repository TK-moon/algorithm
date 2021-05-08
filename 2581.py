m = int(input())
n = int(input())

def isPrime(num):
	if num < 2: return False
	i = 2
	isPrime = True
	while i < num:
		if num % i == 0:
			isPrime = False
			break
		i += 1
	if isPrime:
		return True
	return False

arr = []

for num in range(m, n + 1):
	if isPrime(num):
		arr.append(num)

if len(arr):
	print(sum(arr))
	print(min(arr))
else:
	print(-1)