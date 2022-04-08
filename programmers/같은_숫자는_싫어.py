# 풀이 1:
def solution(arr):
  result = [arr[0]]
  for i in range(0, len(arr)):
    if result[-1] != arr[i]:
      result.append(arr[i])
            
  return result

# 다른 사람 풀이
## 빈 배열에 [-1:] 하면 마지막 값의 배열.. 왜?
def solution(arr):
  result = []
  for i in arr:
    if result[-1:] != [i]:
      result.append(i)
  return result