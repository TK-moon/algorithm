n = int(input())

if n < 0:
  if not n & 1: print('A')
  else: print('B')
else:
  if not n & 1: print('C')
  else: print('D')
