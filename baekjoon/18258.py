from collections import deque
import sys
input = sys.stdin.readline
l = deque([])

for i in range(int(input())):
  command = input().strip().split()
  if command[0] == 'push':
    l.append(command[1])
  elif command[0] == 'pop':
    x = l.popleft() if len(l) else -1
    print(x)
  elif command[0] == 'size':
    print(len(l))
  elif command[0] == 'empty':
    print(0 if len(l) else 1)
  elif command[0] == 'front':
    print(l[0] if len(l) else -1)
  elif command[0] == 'back':
    print(l[-1] if len(l) else -1)