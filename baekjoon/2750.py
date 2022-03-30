repeat = int(input())
arr = []

for i in range(repeat):
  arr.append(int(input()))

arr.sort()
for i in arr:
  print(i)
