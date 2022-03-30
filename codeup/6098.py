table = []
for i in range(10):
  table.append(list(map(int, input().split())))

i = 1
j = 1

while True:
  if table[i][j] == 2:
    table[i][j] = 9
    break

  table[i][j] = 9
  if table[i][j + 1] != 1:
    j += 1
    continue
  elif table[i+1][j] != 1:
    i += 1
    continue
  elif table[i+1][j] == 1 or table[i][j+1] == 1:
    break

for i in table:
  print(*i)