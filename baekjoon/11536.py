repeat = int(input())

arr = []

for _ in range(repeat): arr.append(input())
asc = sorted(arr)
desc = sorted(arr, reverse=True)

if arr == asc: print('INCREASING')
elif arr == desc: print('DECREASING')
else: print('NEITHER')