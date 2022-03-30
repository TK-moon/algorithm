while True:
    sides = list(map(int, input().split()))
    if (sum(sides) == 0):
        break
    max_side = max(sides)
    sides.remove(max_side)
    if sides[0] ** 2 + sides[1] ** 2 == max_side ** 2:
        print('right')
    else:
        print('wrong')
