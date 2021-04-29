repeat = int(input())

for i in range(0, repeat):
	x = input().split()
	print("Case #%d: %s + %s = %d" %(i + 1, x[0], x[1], int(x[0]) + int(x[1])))