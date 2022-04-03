def gcd(a, b):
  while b > 0:
    tmp = a % b
    a, b = b, tmp
  return a

def solution(n, m):
  g = gcd(n, m)
  return [g, n * m / g]