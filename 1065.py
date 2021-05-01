def f(n):
	if n < 100: return True
	arr = list(map(int, str(n)))
	if arr[0] - arr[1] == arr[1] - arr[2]:
		return True
	return False
	


n = int(input())

count = 0

for i in range(1, n + 1):
	if f(i):
		count += 1

print(count)