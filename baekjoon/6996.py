repeat = int(input())

for _ in range(repeat):
  a, b = input().split()
  c, d = map(list, [a, b])
  c.sort()
  d.sort()
  print('{} & {} are '.format(a, b), end='')
  if (c == d): print('anagrams.')
  else: print('NOT anagrams.')