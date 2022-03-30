count = 0
for i in range(8):
  line = input()
  for j in range(8):
    if not i & 1: # 하얀색으로 시작하는 줄
      if not j & 1 and line[j] == 'F': count += 1
    else: # 검은색으로 시작하는 줄
      if j & 1 and line[j] == 'F': count += 1

print(count)