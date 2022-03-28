a = input()
b = input()

arr = []

for i in range(len(a)):
  arr.append(a[i])
  arr.append(b[i])

while True:
  tmp_arr = []
  for i in range(1, len(arr)):
    tmp_arr.append(int(str(int(arr[i-1]) + int(arr[i]))[-1]))
  arr = tmp_arr
  if len(arr) == 2: break

print(''.join(str(i) for i in arr))
