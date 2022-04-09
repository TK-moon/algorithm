def solution(participant, completion):
  dict = {}
  sum_hash = 0
  for i in participant:
    dict[hash(i)] = i
    sum_hash += hash(i)
  
  for i in completion:
    sum_hash -= hash(i)
  
  return dict[sum_hash]
      