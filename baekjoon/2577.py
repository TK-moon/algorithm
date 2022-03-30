A = int(input())
B = int(input())
C = int(input())

mul = list(str(A * B * C))

arr = list()

for i in range(0, 10):
	count = 0
	for j in range(0, len(mul)):
		if (int(mul[j]) == i):
			count += 1
	print(count)