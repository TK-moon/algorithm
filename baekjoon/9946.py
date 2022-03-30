cnt = 1
while True:
  a = input()
  b = input()
  if a == 'END' and b == 'END': break
  a, b = map(list, [a, b])
  a.sort()
  b.sort()
  print('Case {}: '.format(cnt), end='')
  print('same' if a == b else 'different')
  cnt += 1