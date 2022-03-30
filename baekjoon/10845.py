import sys
input = sys.stdin.readline
l = []

for _ in range(int(input())):
  command = input().split()
  if command[0] == 'pop':
    x = l.pop() if len(l) else -1
    print(x)
  elif command[0] == 'size':
    print(len(l))
  elif command[0] == 'empty':
    print(0 if len(l) else 1)
  elif command[0] == 'front':
    x = l[-1] if len(l) else -1
    print(x)
  elif command[0] == 'back':
    x = l[0] if len(l) else -1
    print(x)
  else:
    l.insert(0, int(command[1]))