repeat = int(input())

for _ in range(repeat):
  input()
  count = int(input())
  candy_count = 0
  for i in range(count):
    candy_count += int(input())
  print('YES' if candy_count % count == 0 else 'NO')