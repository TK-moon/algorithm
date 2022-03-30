import sys
input = sys.stdin.readline

a = {}

def dfs (x, y):
  
  over_x = (x <= -1) or (x >= n)
  over_y = (y <= -1) or (y >= n)
  if over_x or over_y: return False

  if matrix[x][y] > 0: # 단지가 존재하면
    global count
    count += 1
    matrix[x][y] = 0
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False


n = int(input())

matrix = []
counts = []

for i in range(n):
  matrix.append(list(map(int, input().strip())))

result = 0
count = 0 # 각 동 카운트

for i in range(n):
  for j in range(n):
    if dfs(i, j):
      counts.append(count)
      result += 1
      count = 0

print(result)
counts.sort()
for i in counts:
  print(i)

# 모든 좌표를 순환
# 한번 방문했던 좌표나 가구가 아니면(0이면) 방문하지 않는다.
# 처음 방문한 좌표와 연결된 모든 노드들을 순환하도록 재귀적으로 함수 호출