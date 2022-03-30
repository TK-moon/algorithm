origin = x = int(input())

count = 0

while True:
	i = x // 10
	j = x % 10

	sum = i + j

	count += 1

	x = int(str(x % 10) + str(sum % 10))

	if (x == origin):
		print(count)
		break
	