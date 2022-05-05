n = int(input())

while True:
  tmp = str(n)
  flag = True
  for i in tmp:
    if i != '4' and i != '7':
      flag = False
      break
  if flag:
    print(n)
    break
  n -= 1