data = {
  'black': { 'value': 0, 'multiple': 1 },
  'brown': { 'value': 1, 'multiple': 10 },
  'red': { 'value': 2, 'multiple': 100 },
  'orange': { 'value': 3, 'multiple': 1000 },
  'yellow': { 'value': 4, 'multiple': 10000 },
  'green': { 'value': 5, 'multiple': 100000 },
  'blue': { 'value': 6, 'multiple': 1000000 },
  'violet': { 'value': 7, 'multiple': 10000000 },
  'grey': { 'value': 8, 'multiple': 100000000 },
  'white': { 'value': 9, 'multiple': 1000000000 },
}

a = str(data[input()]['value'])
b = str(data[input()]['value'])
c = data[input()]['multiple']

print(int(a + b) * c)