n = int(input())

for i in range(0, n):
	arr = list()
	answer = list(input())
	count = 0
	for j in range(0, len(answer)):
		if answer[j] == 'O':
			count += 1
			arr.append(count)
		else:
			count = 0
			arr.append(count)
	print(sum(arr))