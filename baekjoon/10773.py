repeat = int(input())

list = []

for i in range(repeat):
  number = int(input())
  if number != 0:
    list.append(number)
  else:
    list.pop()


print(sum(list))