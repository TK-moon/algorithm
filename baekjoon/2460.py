
l = []

count = 0

for _ in range(10):
  o, i = map(int, input().split())
  count -= o
  count += i
  l.append(count)

print(max(l))