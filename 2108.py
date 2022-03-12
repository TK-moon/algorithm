from collections import Counter
import sys
repeat = int(sys.stdin.readline())

arr = []

for i in range(repeat):
  arr.append(int(sys.stdin.readline()))



# 산술평균
print(round(sum(arr) / len(arr)))


# 중앙값
arr.sort()
print(arr[repeat // 2])


# 최빈값
common_arr = Counter(arr).most_common()
if len(common_arr) > 1:
  if (common_arr[0][1] == common_arr[1][1]):
    print(common_arr[1][0])
  else:
    print(common_arr[0][0])
else:
  print(common_arr[0][0])

# 범위
print(arr[-1] - arr[0])