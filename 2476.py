repeat = int(input())

prices = []

for i in range(repeat):
  a, b, c = map(int, input().split())
  price = 0
  if (a == b == c): price = 10000 + a * 1000
  elif (a == b or b == c): price = 1000 + b * 100
  elif (a == c): price = 1000 + a * 100
  else: price = max(a, b, c) * 100
  prices.append(price)

print(max(prices))