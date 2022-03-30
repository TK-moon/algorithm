odd = []
for _ in range(7):
  num = int(input())
  if num & 1:
    odd.append(num)

if (len(odd)):
  print(sum(odd))
  print(min(odd))
else:
  print(-1)