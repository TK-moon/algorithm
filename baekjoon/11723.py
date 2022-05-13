import sys
input = sys.stdin.readline
r = int(input())

s = set()

for _ in range(r):
  command = input().strip()
  if command == 'all': 
    s = set(i for i in range(1, 21))
    continue
  elif command == 'empty':
    s.clear()
    continue


  exe, x = command.split()
  x = int(x)

  if exe == 'add':
    s.add(x)
  elif exe == 'remove':
    s.discard(x)
  elif exe == 'check':
    print(1 if x in s else 0)
  elif exe == 'toggle':
    if x in s: s.discard(x)
    else: s.add(x)