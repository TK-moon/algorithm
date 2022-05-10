y, x = map(int, input().split())

input_table = []
result_table = []
replace_table = {
  '.': '.',
  'O': 'O',
  '-': '|',
  '|': '-',
  '/': '\\',
  '\\': '/',
  '^': '<',
  '<': 'v',
  'v': '>',
  '>': '^'
}

for _ in range(y):
  input_table.append(list(input()))

for i in range(x):
  tmp = []
  for j in range(y):
    char = replace_table[input_table[j][x-i-1]]
    tmp.append(char)
  result_table.append(tmp)

for i in result_table:
  print(''.join(i))