n = int(input())

for i in range(1, n + 1):
  condition = i % 10 == 3 or i % 10 == 6 or i % 10 == 9
  print('X' if condition else i, end=' ')