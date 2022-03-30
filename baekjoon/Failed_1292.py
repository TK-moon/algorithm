a, b = map(int, input().split())

s = []
for i in range(1, b + 1):
  s += str(i) * i

# print(s)

r = sum(map(int, s[a-1:b]))
print(r)