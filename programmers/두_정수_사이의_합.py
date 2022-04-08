def solution(a, b):
  if a < b: a, b = b, a
  
  n = a - b + 1
  return n * (a + b) / 2