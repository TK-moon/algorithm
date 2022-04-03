import math
def solution(n):
  n = (math.sqrt(n) + 1) ** 2
  return -1 if n % 1 else n