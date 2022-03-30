import sys
input = sys.stdin.readline
repeat = int(input())

coords = []

for i in range(repeat):
  coords.append(list(map(int, input().split())))

coords.sort(key=lambda x: (x[1], x[0]))

for i in coords:
  print(i[0], i[1])