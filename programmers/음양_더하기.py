def solution(absolutes, signs):
  sum = 0
  for i in range(len(signs)):
    sum += absolutes[i] if signs[i] else absolutes[i] * -1
  return sum