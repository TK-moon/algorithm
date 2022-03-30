r = int(input())

s = []

for _ in range(r):
  command = input()
  if command == 'all': 
    s = [i for i in range(1, 21)]
    continue
  elif command == 'empty':
    s.clear()
    continue


  exe, x = command.split()
  x = int(x)

  if exe == 'add':
    s.append(x)
  elif exe == 'remove':
    s.remove(x)
  elif exe == 'check':
    print(1 if x in s else 0)
  elif exe == 'toggle':
    if x in s: s.remove(x)
    else: s.append(x)