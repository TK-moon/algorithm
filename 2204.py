while True:
  repeat = int(input())
  if repeat == 0: break
  arr = []
  for i in range(repeat):
    arr.append(input())
  arr.sort(key=lambda x: x.lower())
  print(arr[0])