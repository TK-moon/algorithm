## 틀린 코드

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
      x = x + dx[i]
      y = y + dy[i]
      over_x = x <= -1 or x >= m
      over_y = y <= -1 or y >= n

      if not over_x and not over_y and land[y][x] == 1:
        land[y][x] = 0
        # print('push', y, x)
        queue.append([x, y])
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
