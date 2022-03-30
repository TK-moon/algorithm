l = list(map(int, input().split()))
s = list(l)
s.sort()

while True:
  if (l[0] > l[1]):
    l[0],l[1] = l[1],l[0]
    print(*l)
  if (l[1] > l[2]):
    l[1],l[2] = l[2],l[1]
    print(*l)
  if (l[2] > l[3]):
    l[2],l[3] = l[3],l[2]
    print(*l)
  if (l[3] > l[4]):
    l[3],l[4] = l[4],l[3]
    print(*l)
  if l == s: break