def solution(s):
  length = len(s)
  half = length // 2
  return s[half] if length & 1 else s[half - 1 : half + 1]