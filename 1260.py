from os import sep
import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v):
  dfs_visited[v] = True
  dfs_list.append(v)
  for i in graph[v]:
    if not dfs_visited[i]:
      dfs(graph, i)


def bfs(graph, v):
  queue = deque([v])
  bfs_visited[v] = True
  while queue:
    v = queue.popleft()
    bfs_list.append(v)
    for i in graph[v]:
      if not bfs_visited[i]:
        queue.append(i)
        bfs_visited[i] = True


n, m, v = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
# graph = [[]] * (m + 1)
# graph = [[] * (m + 1)]
# 위 코드는 동작하지 않는다. 이유가 뭐지 뭐가 다른거지

for i in range(m):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  graph[b].append(a)

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

# graph.sort() 로 내부까지 정렬되지 않는다. 왜지?
for i in range(1, len(graph)):
  graph[i].sort()

dfs_list = []
bfs_list = []

dfs(graph, v)
bfs(graph, v)

print(*dfs_list, sep=' ')
print(*bfs_list, sep=' ')