n = int(input())

l = list(map(int, input().split()))
r = []

tmp = 0

for i in range(n):
  if l[i] == 1:
    score = l[i] + tmp
    tmp += 1
    r.append(score)
  else:
    tmp = 0
    r.append(0)

print(sum(r))