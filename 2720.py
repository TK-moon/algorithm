repeat = int(input())

for _ in range(repeat):
  change = int(input())
  a = change // 25
  change = change % 25
  b = change // 10
  change = change % 10
  c = change // 5
  change = change % 5
  d = change // 1
  change = change % 1
  print(a, b, c, d)