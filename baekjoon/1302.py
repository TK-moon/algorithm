n = int(input())
d = {}

for i in range(n):
  book = input()
  if book in d: d[book] += 1
  else: d[book] = 1

r = sorted(d.items(), key=lambda x: (-x[1], x[0]))

print(r[0][0])