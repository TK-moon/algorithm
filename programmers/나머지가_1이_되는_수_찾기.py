def solution(n):
  div = 1
  while n > div:
    if n % div == 1:
      return div
    div += 1