import sys
sys.setrecursionlimit(10**6)

def dfs(node): #dfs수행
    for i in graph[node]: # 현재 노드에 연결된 모든 i를 순회
        if visited[i] == False: #i노드가 아직 방문 안했을 경우 확인
            visited[i] = node #노드의 부모 노드를 node로 설정
            dfs(i) #재귀적으로 i계속 수향

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)] #각 노드의 연결된 노드를 저장할 인접 리스트 생성. 인덱스를 1부터 사용하기 위해 N+1크기로 만듦
for _ in range(N-1): #트리의 간선정보를 입력받는다. 간선은 항상 N-1개의 간선을 가짐
    a,b = map(int,input().split()) #두 노드 a,b를 받아 간선을 추가
    graph[a].append(b) # 양방향 간선을 추가하여 인접 리스트 업데이트
    graph[b].append(a)

visited = [False]*(N+1) # 방문 여부와 부모 노드를 저장할 리스트를 초기화한다. 인덱스를 1부터 사용하기 위해 N+1크기로 만듦

dfs(1) #루트 노드인 1번 노드부터 dfs시작

for x in range(2,N+1): # 2번 노드부터 N번 노드까지 순회
    print(visited[x]) # 각 노드의 부모 노드 출력
