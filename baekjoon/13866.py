arr = list(map(int, input().split()))
arr.sort()

a = arr[0] + arr[3]
b = arr[1] + arr[2]

print(abs(a - b))