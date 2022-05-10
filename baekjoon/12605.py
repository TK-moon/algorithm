repeat = int(input())

for i in range(repeat):
  string = input().split(' ')
  string.reverse()
  print('Case #{0}: {1}'.format(i + 1, ' '.join(string)))