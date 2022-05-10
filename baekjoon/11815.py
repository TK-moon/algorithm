case = int(input())
numbers = list(map(int, input().split()))

for x in numbers:
  if x == int(x ** 0.5) ** 2:
    print(1, end=' ')
  else:
    print(0, end=' ')