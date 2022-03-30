a, b, c = map(int, input().split())

count = 0
for i in range(0, a):
  for j in range(0, b):
    for k in range(0, c):
      print(i, j ,k)
      count += 1

print(count)