def getFirst(n):
  if n == 1: return 500
  if 1 < n <= 3: return 300
  if 3 < n <= 6: return 200
  if 6 < n <= 10: return 50
  if 10 < n <= 15: return 30
  if 15 < n <= 21: return 10
  return 0

def getSecond(n):
  if n == 1: return 512
  if 1 < n <= 3: return 256
  if 3 < n <= 7: return 128
  if 7 < n <= 15: return 64
  if 15 < n <= 31: return 32
  return 0

repeat = int(input())
for _ in range(repeat):
  a, b = map(int, input().split())
  a = getFirst(a)
  b = getSecond(b)
  print((a + b) * 10000)