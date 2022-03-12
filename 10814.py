import sys
input = sys.stdin.readline

repeat = int(input())

arr = []

for i in range(repeat):
  [age, name] = input().split()
  arr.append([int(age), name])

arr.sort(key=lambda x: x[0])

for i in arr:
  print(i[0], i[1])