## First
# stack = list()

# def push(value):
#   return stack.append(value)

# def pop():
#   if (len(stack) == 0): return -1
#   return stack.pop()

# def empty():
#   if len(stack) > 0: return 0
#   else: return 1

# def top():
#   length = len(stack)
#   if (length < 1): return -1
#   return stack[length - 1]

# num = int(input())

# for i in range(0, num):
#   user_input = input()
#   command = ''
#   value = ''

#   if (user_input.find(' ') != -1):
#     command = user_input.split(' ')[0]
#     value  = user_input.split(' ')[1]
#   else: command = user_input

#   if command == 'push':
#     push(value)
#   elif command == 'pop':
#     print(pop())
#   elif command == 'size':
#     print(len(stack))
#   elif command == 'empty':
#     print(empty())
#   elif command == 'top':
#     print(top())


import sys

stack = []
num = int(sys.stdin.readline())

for i in range(num):
  command = sys.stdin.readline().split()

  if command[0] == 'push':
    stack.append(command[1])
  elif command[0] == 'pop':
    if len(stack) == 0: print(-1)
    else: print(stack.pop())
  elif command[0] == 'size':
    print(len(stack))
  elif command[0] == 'empty':
    if len(stack) > 0: print(0)
    else: print(1)
  elif command[0] == 'top':
    if len(stack) == 0: print(-1)
    else: print(stack[len(stack)-1])