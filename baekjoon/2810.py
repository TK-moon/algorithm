n = int(input())
line = input()

cnt = 1
i = 0

while i < len(line):
  if line[i] == 'S':
    cnt += 1
    i+= 1
  elif line[i] == 'L':
    cnt += 1
    i += 2

print(min(n, cnt))