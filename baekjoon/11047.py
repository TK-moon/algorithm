[count, price] = list(map(int, input().split(' ')))

coin_types = []
coin_count = 0

for i in range(count):
  coin_types.append(int(input()))

coin_types.sort(reverse=True)

for coin in coin_types:
  if price // coin > 0:
    coin_count += price // coin
    price = price - (coin * (price // coin))

print(coin_count)