n, m = map(int, input().split())

d = {}

for i in range(n):
  site, password = input().split()
  d[site] = password

for i in range(m):
  key = input()
  print(d[key])