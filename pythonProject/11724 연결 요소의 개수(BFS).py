import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(graph, start, visited):
    # 그래프를 나타내는 인접 리스트, BFS를 시작할 노드의 인덱스,
    # 방문 노브를 나타내는 불리언 리스트로, 인덱스는 그래프의 각 노드를 가리킨다.
    queue = [start] # BFS를 위한 큐를 초기화하고, 시작 노드 start를 큐에 넣는다.
    visited[start] = True
    # 시작 노드 start를 방문 했음을 표시하기 위해 visited리스트의 해당 인덱스를 True로 설정한다.
    while queue: # 큐가 비어있지 않은 동안 반복한다.
        start = queue.pop(0) # 큐에서 첫 번째 요소를 꺼내서 start변수에 할당한다. 이는 BFS의 현재 노드를 나타낸다.
        for i in graph[start]: # 현재 노드 start에 연결된 모든 인접 노드들에 대해 반복한다.
            if not visited[i]: # 인접 노드 i가 방문되지 않았으면 (즉, visited[i]가 False일 때
                queue.append(i) # 큐에 인접 노드 i를 추가하여 BFS의 다음 단계에서 탐색 할 수 있도록 준비한다.
                visited[i] = True # 인접 노드 i를 방문했음을 표시하기 위해 visited 리스트의 해당 인덱스를 True로 설정한다.

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m): #간선을 돌리는 반복문
    a,b = map(int,input().split()) # 간선이 어느 정점과 어느 정점이 이어져 있는지 알아볼 수 있다.
    graph[a].append(b) # 무방향 그래프에서 사용할 수 있음. 예를 들어 1과 2와 이어져 있는 걸 1을 정점 노드에서 확인 했기 때문에 2번을 정점 노드로 했을떄 1번이 인접한 정점인지 확인할 필요가 없음.
    graph[b].append(a)

visited = [False]*(n+1) #visited라는 리스트 안을 전부 False로 채움
cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        cnt += 1
        bfs(graph, i , visited)

print(cnt)