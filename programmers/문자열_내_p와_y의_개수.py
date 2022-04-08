def solution(s):
  s = s.upper()
  p = s.count('P')
  y = s.count('Y')
  return True if p == y else False