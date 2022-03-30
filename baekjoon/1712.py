fixed, prod_cost, price = map(int, input().split())

if prod_cost >= price: print(-1)
else:
	print(int(fixed / (price - prod_cost) + 1))


# 1000 - 170 + 70 = -900
# 1000 - 340 + 140 = -800
# 1000 - 510 + 210 = -700