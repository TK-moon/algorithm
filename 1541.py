import sys
input = sys.stdin.readline

arr = input().strip().split('-')
numbers = []

for i in arr:
  number = sum(map(int, i.split('+')))
  numbers.append(number)

cnt = numbers[0]
for i in numbers[1:]:
  cnt -= i

print(cnt)