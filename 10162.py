time = int(input())

a = 5 * 60
b = 1 * 60
c = 10
if (time % 10 != 0):
  print(-1)
else:
  print(time // a)
  print((time % a) // b)
  print(((time % a) % b) // c)