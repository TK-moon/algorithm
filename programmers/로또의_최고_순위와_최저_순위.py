def solution(lottos, win_nums):
  lottos.sort()
  win_nums.sort()
  
  win_table = [6, 6, 5, 4, 3, 2, 1]
  
  count1 = 0
  count2 = 0
  
  for i in lottos:
    if i in win_nums: count1 += 1
    if i == 0: count2 += 1
      
  count2 += count1
  
  
  result = [win_table[count2], win_table[count1]]
  
  return result