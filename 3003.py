origin_count = [1, 1, 2, 2, 2, 8]
real_count = list(map(int, input().split()))

arr = []

for i in range(len(origin_count)):
  arr.append(origin_count[i] - real_count[i])

print(*arr)