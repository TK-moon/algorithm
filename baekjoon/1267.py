import math
def Y(m): return math.ceil((m + 1) / 30) * 10

def M(m): return math.ceil((m + 1) / 60) * 15

input()
l = list(map(int, input().split()))

y = 0
m = 0

for i in l:
  y += Y(i)
  m += M(i)

if y < m: print('Y', y)
elif y > m: print('M', m)
else: print('Y M', y)