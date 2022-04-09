def solution(s):
  arr = []
  for i in s:
    if arr[-1:] == [i]:
      arr.pop()
    else: arr.append(i)

  return 1 if not len(arr) else 0