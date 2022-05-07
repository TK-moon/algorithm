while True:
  n = input()
  if n == '0': break

  repeat = len(n) // 2
  if len(n) & 1: repeat += 1

  flag = 'yes'
  for i in range(repeat):
    a = n[i]
    b = n[len(n)-(i+1)]
    if a != b: flag = 'no'

  print(flag)

# 리팩토링
## 뒤집어서 똑같으면 펠린드롬 수
while True:
  n = input()
  if n == '0': break
  
  if n == n[::-1]: print('yes')
  else: print('no')