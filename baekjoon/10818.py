# input()
# arr = list(map(int, input().split()))

# print(min(arr), max(arr))

length = int(input())
arr = list(map(int, input().split()))

min = arr[0];
max = arr[0];

for i in range(0, length):
	if (min > arr[i]):
		min = arr[i]
	if(max < arr[i]):
		max = arr[i]

print(min, max)