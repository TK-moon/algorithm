import sys
input = sys.stdin.readline

repeat = int(input())

for i in range(repeat):
  a, b = map(int, input().strip().split())
  num = a ** b
  print(str(num)[-1])

# 시간초과