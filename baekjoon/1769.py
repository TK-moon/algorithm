n = input()
count = 0
while len(n) != 1:
  n = str(sum(map(int, n)))
  count += 1

print(count)
print('YES' if int(n) % 3 == 0 else 'NO')
