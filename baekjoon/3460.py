repeat = int(input())
for _ in range(repeat):
  n = reversed(bin(int(input()))[2:])
  for i, d in enumerate(n):
    if d == '1': print(i, end=' ')