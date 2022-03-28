n, l, h = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
arr = arr[l: n-h]

print(sum(arr) / (n - (l + h)))