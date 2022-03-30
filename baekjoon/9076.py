repeat = int(input())

for i in range(repeat):
  arr = list(map(int, input().split()))
  arr.sort()
  arr = arr[1:4]
  if max(arr) - min(arr) >= 4: print('KIN')
  else: print(sum(arr))