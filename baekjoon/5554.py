arr = []
for i in range(4):
  arr.append(int(input()))

time = sum(arr)
print(time // 60)
print(time % 60)