repeat = int(input())

for i in range(0, repeat):
	n, s = input().split()
	n = int(n)
	for i in s:
		print(i * n, end='')
	print()