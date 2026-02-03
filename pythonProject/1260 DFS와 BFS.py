N,M,V = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0]*(N+1) # 각 노드가 방문되었는지 여부를 기록하는 데 사용
visited2 = visited1.copy()

def dfs(V):
    visited1[V] = True
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] == True and visited1[i] == False:
            dfs(i)

def bfs(V):
    queue = [V] #현재 정점 초기값(1)
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end =' ')
        for i in range(1, N+1):
            if(graph[V][i] == 1 and visited2[i] == 0):
                # 1. 정점 v와 정점 i가 연결 되어 있어야 합니다.
                # 2. 정점 i가 아직 방문 되지 않았어야 합니다.
                queue.append(i)
                visited2[i] = 1

# dfs(V)
print()
bfs(V)

