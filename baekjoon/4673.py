def d(n: int):
	n = n + sum(list(map(int, str(n))))
	return n

arr = list()

for i in range(1, 10001):
	arr.append(d(i))

arr.sort()

for i in range(1, 10001):
	if i in arr:
		pass
	else:
		print(i)