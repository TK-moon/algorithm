while True:
  numbers = input()
  if numbers == '0': break
  length = 0
  for i in numbers:
    if i == '1': length += 2
    elif i == '0': length += 4
    else: length += 3
  length += 2
  length += len(numbers) - 1
  print(length)