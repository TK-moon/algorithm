n, m = map(int, input().split())

# for i in range(m):
#   for j in range(n):
#     print('*', end='')
#   print()

# for i in range(m):
#     print('*' * n)

answer = ('*' * n +'\n') * m
print(answer)