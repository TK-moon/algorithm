star = int(input())

for x in range(star):
	for i in range(star - 1, x, -1):
		print(' ', end='')
	for j in range(x + 1):
		print('*', end='')
	print()