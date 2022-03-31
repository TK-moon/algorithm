l = []

for _ in range(int(input())):
  line = list(input().split())
  line[1:] = list(map(int, line[1:]))
  l.append(line)

l.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in l:
  print(i[0])