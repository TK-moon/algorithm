def solution(price, money, count):
  pay = 0
  for i in range(1, count + 1):
    pay += i * price
  return max(pay - money, 0)