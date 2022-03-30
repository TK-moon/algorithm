n = int(input())
count = 1
sum = 0
while True:
  sum += count
  if sum >= n: break
  count += 1

print(count)