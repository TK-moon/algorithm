table = []
for i in range(19):
  table.append(list(map(int, input().split())))

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  x = x - 1
  y = y - 1
  for j in range(19):
    table[x][j] = int(not table[x][j])

  for j in range(19):
    table[j][y] = int(not table[j][y])

for i in table:
  print(*i)