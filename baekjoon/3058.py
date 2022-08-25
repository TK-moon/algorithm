n = int(input())
for _ in range(n):
  l = list(filter(lambda x: not x & 1,map(int, input().split())))
  print(sum(l), min(l))
