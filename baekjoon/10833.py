repeat = int(input())

acc = 0

for i in range(repeat):
  a, b = map(int, input().split())
  acc += b % a

print(acc)