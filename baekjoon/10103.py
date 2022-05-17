repeat = int(input())

a = b = 100

for _ in range(repeat):
  n, m = map(int, input().split())
  if n > m: b -= n
  elif n < m: a -= m

print(a)
print(b)