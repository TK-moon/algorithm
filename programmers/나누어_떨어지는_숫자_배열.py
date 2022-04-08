def solution(arr, divisor):
  result = []
  for i in arr:
    if i % divisor == 0:
      result.append(i)
          
  result.sort()
  return result or [-1]