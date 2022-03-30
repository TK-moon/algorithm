h, w = map(int, input().split())
table = [[0 for i in range(w)] for j in range(h)]

repeat = int(input())

for i in range(repeat):
  l, d, x, y = map(int, input().split())
  x = x - 1
  y = y - 1
  for j in range(l):
    if d == 0: # 가로
      table[x][y+j] = 1
    if d == 1: # 세로
      table[x+j][y] = 1

for i in table:
  print(*i)