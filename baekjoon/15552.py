import sys
input = sys.stdin.readline

repeat = int(input())

for i in range(repeat):
	x = input().split()
	print(int(x[0]) + int(x[1]))
