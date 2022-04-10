table = {
  'ascending': list(range(1, 9)),
  'descending': list(range(8, 0, -1))
}

l = list(map(int, input().split()))

if l == table['ascending']: print('ascending')
elif l == table['descending']: print('descending')
else: print('mixed')