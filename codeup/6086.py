n = int(input())

count = 1
s = 0
while True:
  s += count
  if s >= n: break
  count += 1

print(s)