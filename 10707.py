xd = int(input())
yd = int(input())
yl = int(input())
ya = int(input())
p = int(input())

x = p * xd

y = 0
if (p <= yl): y = yd
elif (p > yl):
  use = p - yl
  y += yd + use * ya

print(min(x, y))