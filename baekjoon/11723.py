import sys
input = sys.stdin.readline
r = int(input())

s = set()
reset_set = set(i for i in range(1, 21))

for _ in range(r):
  command = input().strip()
  if command == 'all': 
    s = reset_set
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