# 처음 짠 코드
n = int(input())
cards = []

for _ in range(n):
  cards.append(int(input()))

cards.sort()
s = set(cards)

r = {}
for i in s: r[i] = 0
for i in cards: r[i] += 1

r = sorted(r.items(), key=lambda x: (-x[1], x[0]))

print(r[0][0])



# 리팩토링
n = int(input())
d = {}

for _ in range(n):
  x = int(input())
  if x in d: d[x] += 1
  else: d[x] = 1

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

print(d[0][0])