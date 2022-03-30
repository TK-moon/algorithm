a = 0
b = 0

for i in range(5):
  arr = list(map(int, input().split()))
  arr_sum = sum(arr)
  if a < arr_sum:
    a = arr_sum
    b = i + 1
print(b, a)