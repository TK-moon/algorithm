def solution(arr):
  m = min(arr)
  arr.remove(m)
  return arr or [-1]