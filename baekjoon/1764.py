n, m = map(int, input().split())

l1 = []
l2 = []

for i in range(n):
  l1.append(input())

for i in range(m):
  l2.append(input())

rl = list(set(l1) & set(l2))
rl.sort()

print(len(rl))

for i in rl:
  print(i)