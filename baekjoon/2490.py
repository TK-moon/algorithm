for i in range(3):
  game = list(map(int, input().split()))
  count = game.count(1)

  if count == 0: print('D')
  elif count == 1: print('C')
  elif count == 2: print('B')
  elif count == 3: print('A')
  else: print('E')

