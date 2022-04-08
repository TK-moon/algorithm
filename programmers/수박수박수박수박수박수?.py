def solution(n):
  result = ''
  for i in range(n):
    result += '박' if i & 1 else '수'
  return result