arr = list()

for i in range(0, 10):
	arr.append(int(input()) % 42)

arr = set(arr)

print(len(arr))