n = int(input())

while True:
  m = int(input())
  if m == 0: break
  if m % n: print('{0} is NOT a multiple of {1}.'.format(m, n))
  else: print('{0} is a multiple of {1}.'.format(m, n))