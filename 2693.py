repeat = int(input())
for _ in range(repeat):
  arr = list(map(int, input().split()))
  arr.sort(reverse=True)
  print(arr[2])