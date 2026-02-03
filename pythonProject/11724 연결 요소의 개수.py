
# dfs(탐색할 그래프, 시작 노드, 방문여부 리스트)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(graph, i, visited)
print(cnt)