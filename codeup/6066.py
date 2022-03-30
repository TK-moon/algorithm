l = map(int, input().split())
for i in l:
  print('odd' if i & 1 else 'even')