n = int(input())

def getTextByBottleCount(count):
  if count > 1: return '{} bottles'.format(count)
  elif count == 1: return '1 bottle'
  return 'no more bottles'

for i in range(n):
  string = '''{0} of beer on the wall, {0} of beer.
Take one down and pass it around, {1} of beer on the wall.'''

  current = getTextByBottleCount(n - i)
  next = getTextByBottleCount(n) if i == n else getTextByBottleCount(n - i - 1)
  print(string.format(current, next))
  print()

print('''No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, {} of beer on the wall.'''.format(getTextByBottleCount(n)))