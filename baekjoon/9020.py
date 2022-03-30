table = [False, False] + [True] * 10000  
for i in range(2, 101):
    if table[i] == True:
        for j in range(i + i, 10001, i):
            table[j] = False

repeat = int(input())

for _ in range(repeat):
  n = int(input())

  # 이부분이 이해가 안된다.
  a = n // 2
  b = a

  while True:
    if table[a] and table[b]:
      print(a, b)
      break
    a -= 1
    b += 1