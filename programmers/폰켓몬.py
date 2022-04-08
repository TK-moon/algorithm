def solution(nums):
  choose = len(nums) // 2
  
  count = len(list(set(nums)))
  return min(choose, count)