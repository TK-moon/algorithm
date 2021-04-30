x = int(input())

origin = x

if x < 10:
	x = ['0', str(x)]
else:
	x = list(str(x))

count = 0

while True:
	y = sum(list(map(int, x)))
	y = list(str(y))
	y = y[len(y) - 1]
	new = str(x[1]) + str(y)

	x = list(map(int, list(str(new))))

	count += 1

	if int(str(x[0]) + str(x[1])) == origin:
		print(count)
		break