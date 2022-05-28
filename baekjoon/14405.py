string = input()

pikachu = ['pi', 'ka', 'chu']

for i in pikachu: string = string.replace(i, ' ')
string = string.strip()

print('NO' if string else 'YES')