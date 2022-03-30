n = int(input())

cnt = 1
s = 0
while True:
  s += cnt
  if s > n: break
  cnt += 1

print(cnt - 1)

# 이런 생각은 어떻게 하는건가