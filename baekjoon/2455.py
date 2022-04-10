count = 0
l = []
for i in range(4):
  o, i = map(int, input().split())
  count -= o
  count += i
  l.append(count)

print(max(l))