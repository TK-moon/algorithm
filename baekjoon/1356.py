from functools import reduce
n = input()

flag = 'NO'
for i in range(1, len(n)):
  a = int(reduce(lambda acc, cur: int(acc) * int(cur), n[:i]))
  b = int(reduce(lambda acc, cur: int(acc) * int(cur), n[i:]))
  
  if a == b:
    flag = 'YES'
    break

print(flag)