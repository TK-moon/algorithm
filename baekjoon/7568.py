repeat = int(input())
l = []
for _ in range(repeat):
  l.append(list(map(int, input().split())))
rank = []
for i in l:
  count = 1
  for j in l:
    if (j[0] > i[0] and j[1] > i[1]): count += 1
  rank.append(count)

print(*rank)