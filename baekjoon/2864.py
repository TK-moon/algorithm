a, b = input().split()

mina = a.replace('6', '5')
minb = b.replace('6', '5')
min_sum = sum([int(mina), int(minb)])

maxa = a.replace('5', '6')
maxb = b.replace('5', '6')
max_sum = sum([int(maxa), int(maxb)])

print(min_sum, max_sum)