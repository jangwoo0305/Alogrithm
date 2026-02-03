# N,M,V = map(int,input().split())
#
# graph = [[0]*(N+1) for _ in range(N+1)]
# for i in range(M):
#     a,b = map(int,input().split())
#     graph[a][b] = graph[b][a] = 1
#
# visited1 = [0]*(N+1)
# visited2 = visited1.copy()
#
# def dfs (V):
#     visited1[V] = 1
#     print(V, end=' ')
#     for i in range(1, N+1):
#         if graph[V][i] == 1 and visited1[i] == 0:
#             dfs(i)

import sys

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx,end=' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


input = sys.stdin.readline
N, M, V = map(int,input().split())

graph = [[False]*(N+1)for _ in range(N+1)]
visited = [False]*(N+1)

# 1. graph정보 입력
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

#dfs
dfs(V)
print()

#bfs
visited = [False]*(N+1)
q = [V]
visited[V] = True
bfs()