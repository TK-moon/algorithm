fibo_list = [None] * 46

def fibo(n):
  if fibo_list[n]: return fibo_list[n]

  if n == 0:
    fibo_list[0] = 0
    return 0
  if n == 1 or n == 2:
    fibo_list[n] = 1
    return 1

  f = fibo(n-2) + fibo(n-1)
  fibo_list[n] = f
  return f

n = int(input())
print(fibo(n))