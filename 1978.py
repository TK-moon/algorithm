input()

arr = list(map(int, input().split()))

count = 0

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

for number in arr:
	if isPrime(number): count += 1

print(count)
