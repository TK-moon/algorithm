n = int(input())

arr = list(map(int, input().split()))

max = max(arr)

for i in range(0, len(arr)):
	arr[i] = arr[i] / max * 100

print(sum(arr) / len(arr))