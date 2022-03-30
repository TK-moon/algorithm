a, d, n = map(int, input().split())

count = 1
while True:
  if count == n: break
  a += d
  count += 1

print(a)