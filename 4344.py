repeat = int(input())

for i in range(0, repeat):
	user_input = list(map(int, input().split()))
	n = user_input[0]
	arr = user_input[1:]
	
	avg = sum(arr) / len(arr)
	upper_avg_count = 0

	for j in range(0, len(arr)):
		if arr[j] > avg: upper_avg_count += 1

	print('%.3f%%' % (upper_avg_count / len(arr) * 100))