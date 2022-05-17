n = int(input())

for i in range(n):
  r, e, c = map(int, input().split())
  a = r
  b = e - c
  if a > b: print('do not advertise')
  elif a < b: print('advertise')
  else: print('does not matter')