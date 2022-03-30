a, m, d, n = map(int, input().split())

count = 1
while True:
  if count == n: break
  a = a * m + d
  count += 1

print(a)