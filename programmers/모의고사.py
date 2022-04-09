def solution(answers):
    
  a = [1, 2, 3, 4, 5]
  b = [2, 1, 2, 3, 2, 4, 2, 5]
  c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
      
  count = [0, 0, 0]
  
  for index, value in  enumerate(answers):
    if a[index % len(a)] == value:
      count[0] += 1
    if b[index % len(b)] == value:
      count[1] += 1
    if c[index % len(c)] == value:
      count[2] += 1
  
  max_correct_count = max(count)
  result = []
  
  for i in range(len(count)):
    if count[i] == max_correct_count:
      result.append(i + 1)
  
  return result
  