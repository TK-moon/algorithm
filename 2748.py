# 시간초과
# def fibo(n):
#   if n == 0: return 0
#   if n == 1: return 1
#   return fibo(n-2) + fibo(n-1)

# n = int(input())
# print(fibo(n))

# 풀이

n = int(input())
fibo = []
for i in range(n + 1):
  if (i == 0): fibo.append(0)
  elif (i == 1): fibo.append(1)
  else: fibo.append(fibo[-1] + fibo[-2])

print(fibo[-1])