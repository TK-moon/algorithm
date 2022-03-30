import sys
input = sys.stdin.readline

def dfs(graph, v):
  dfs_visited[v] = True
  for i in graph[v]:
    if not dfs_visited[i]:
      dfs(graph, i)

computer = int(input())
line = int(input())

graph = [[] for i in range(computer + 1)]
dfs_visited = [False] * (computer + 1)

for i in range(line):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(graph, 1)
dfs_visited[1] = False
print(sum(dfs_visited))