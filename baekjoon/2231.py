from curses.ascii import NUL


n = int(input())

result = 0
for i in range(1, n + 1):
  a = i
  b = sum(map(int, str(i)))
  if a + b == n:
    result = i
    break

print(result)