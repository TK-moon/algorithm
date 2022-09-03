import sys
input = sys.stdin.readline

repeat = int(input())

obj = {}

for _ in range(repeat):
  [name, command] = input().strip().split()
  if command == 'enter': obj[name] = True
  else: del obj[name]

l = [i for i in obj]
l.sort(reverse=True)

for i in l:
  print(i)