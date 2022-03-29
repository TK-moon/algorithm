# 실패 코드
n = input()
cnt = 0
while True:
  x = sum(map(int, list(n)))
  n = str(x)
  cnt += 1
  if len(str(x)) == 1: break

print(cnt)
print('YES' if int(n) % 3 == 0 else 'NO')

