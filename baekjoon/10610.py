import itertools

n = list(input())

n.sort(reverse=True)

if '0' not in n: print(-1)
else:
  s = sum(map(int, n))
  if s % 3 != 0:
    print(-1)
  else:
    print(''.join(n))