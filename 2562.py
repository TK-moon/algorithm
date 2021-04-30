arr = list()

for i in range(0, 9):
	arr.append(int(input()))

max = arr[0]
index = 0

for i in range(0, 9):
	if (arr[i] > max):
		max = arr[i]
		index = i

print(max, index + 1)