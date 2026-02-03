def dsf(V):
    visited[V] = True
    global cnt
    cnt +=1
    for i in graph[V]:
        if not visited[i]:
            dsf(i)

C = int(input())
L = int(input())

graph = [[] for _ in range(C+1)]

for i in range(L):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(C+1)
cnt = 0

dsf(1)
print(cnt-1)