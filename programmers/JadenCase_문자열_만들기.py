def solution(s):
  result = s[0].upper()
  for i, d in enumerate(s[1:]):
    i += 1
    if s[i-1] == ' ': result += s[i].upper()
    else: result += s[i].lower()
  
  return result