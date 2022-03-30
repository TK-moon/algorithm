price, count, wallet = map(int, input().split())
print(abs(min(wallet - price * count, 0)))