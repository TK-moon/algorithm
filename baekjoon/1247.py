import sys
input = sys.stdin.readline

for _ in range(3):
  repeat = int(input())
  arr = []
  for i in range(repeat):
    arr.append(int(input()))
  
  sum_arr = sum(arr)
  if (sum_arr > 0): print('+')
  elif (sum_arr < 0): print('-')
  else: print('0')
  