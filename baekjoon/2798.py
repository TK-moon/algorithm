from itertools import *
n, m = map(int, input().split())
l = list(map(int, input().split()))

cb = list(combinations(l, 3))

result = 0
for i in cb:
  if result < sum(i) <= m: result = sum(i)
  if result == m: break

print(result)