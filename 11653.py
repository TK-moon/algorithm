n = int(input())

arr = []

while n > 1:
	i = 2
	while True:
		if n % i == 0:
			arr.append(i)
			n = n / i
			break;
		i += 1

for i in sorted(arr):
	print(i)