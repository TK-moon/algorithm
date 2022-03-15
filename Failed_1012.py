import sys
from collections import deque
input = sys.stdin.readline


repeat = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS로 풀어야 함
# DFS로 풀면 메모리 초과 출력
def bfs(x, y):
  queue = deque()
  queue.append([x, y])
  land[y][x] = 0

  while queue:
    [x, y] = queue.popleft()
    # print('call', y, x)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      over_x = nx <= -1 or nx >= m
      over_y = ny <= -1 or ny >= n
      if over_x or over_y:
        continue
      if land[ny][nx] == 0:
        continue
      if land[ny][nx] == 1:
        land[ny][nx] = 0
        # print('push', y, x)
        queue.append([nx, ny])
  # print()

for _ in range(repeat):
  m, n, cab = map(int, input().strip().split())
  land = [[0] * m for i in range(n)]

  for _ in range(cab):
    x, y = map(int, input().strip().split())
    land[y][x] = 1

  # for i in land:
  #   print(i)
  
  count = 0
  for row in range(n):
    for column in range(m):
      if land[row][column] == 1:
        bfs(column, row)
        count += 1

  print(count)
