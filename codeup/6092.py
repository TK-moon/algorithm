n = int(input())
call = list(map(int, input().split()))

count = [0] * 23

for i in range(n):
  index = call[i] - 1
  count[index] += 1

print(*count)