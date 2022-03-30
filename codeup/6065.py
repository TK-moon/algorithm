l = list(map(int, input().split()))

for i in l:
  if not i & 1: print(i)