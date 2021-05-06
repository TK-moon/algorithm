import math
a, b, v = map(int, input().split())

# day = 1
# height = 0

# while True:
# 	height += a
# 	if height >= v:
# 		break;
# 	height -= b
# 	day += 1;

# print(day);

day = math.ceil((v - b) / (a - b))
print(day)