import itertools

def solution(numbers):
  l = list(map(sum, itertools.combinations(numbers, 2)))
  result = set()
  for i in l:
    result.add(i)
      
  return sorted(result)