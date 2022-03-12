import sys
input = sys.stdin.readline
repeat = int(input())

coords = []

for i in range(repeat):
  coords.append(list(map(int, input().split())))

coords.sort()
# coords.sort(key=lambda x: (x[0], x[1]))

for i in coords:
  print(i[0], i[1])