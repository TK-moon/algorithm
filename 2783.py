arr = []
arr.append(list(map(int, input().split())))

repeat = int(input())
for i in range(repeat):
  arr.append(list(map(int, input().split())))

arr2 = []
for i in arr:
  x = i[0]
  y = i[1]
  g = x / y
  arr2.append(g * 1000)

print("{:2}".format(min(arr2)))