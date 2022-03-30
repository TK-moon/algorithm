n = input()
m = int(n, 16)

for i in range(1, 16):
  print('{0:X}*{1:X}={2:X}'.format(m, i, i*m))