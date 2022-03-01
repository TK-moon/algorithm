repeat = int(input())

for i in range(repeat):
  str = input()
  status = []
  
  for j in str:
    if j == '(': status.append(1)
    else: status.append(-1)
  
  count = 0
  for i in status:
    count += i
    if count < 0:
      count = 2
      break
  
  print('YES' if sum(status) == 0 and count == 0 else 'NO')
