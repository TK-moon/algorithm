import sys
input = sys.stdin.readline

repeat = int(input())

con = []

for i in range(repeat):
  con.append(list(map(int, input().strip().split())))

con.sort(key=lambda x: (x[1], x[0]))
# https://suri78.tistory.com/26
# 위 풀이 참고
# 모든 경우의 수를 예상하는게 너무 어렵다

cons = []

finish_time = 0
for i in con:
  [a, b] = i
  if a >= finish_time:
    finish_time = b
    cons.append([a, b])

print(len(cons))