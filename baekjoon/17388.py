l = list(map(int, input().split()))

if sum(l) >= 100:
  print('OK')
else:
  m = min(l)
  if l[0] == m: print('Soongsil')
  elif l[2] == m: print('Hanyang')
  else: print('Korea')
  