# parent = 서로소 집합 개념에서 각 정점이 어느 집합에 속해있는지 정보를 저장
# edges = 간선의 정보를 저장하는 공간, 가장 작은 비용이 발생하는 간선부터 연결해나간다.
# find_parent = 해당하는 정점의 부모(집합)를 찾아주는 함수
# union_parent = 두 정점에 대해서 같은 부모(집합)에 속할 수 있도록 연산, 더 작은 값이 부모가 된다.

import sys
input = sys.stdin.readline
V, E = map(int,input().split())
edges = []

for i in range(E):
    s, e, w = map(int,input().split())
    edges.append((w, s, e))

def f_parent(x): # 최상위 부모를 찾게 만든다
    if parent[x] != x:
        parent[x] = f_parent(parent[x]) #계속 집어넣어보면 되지 않을까..?
    return parent[x]

def mix_parent(s,e):
    s = f_parent(s)
    e = f_parent(e)
    if s < e:
        parent[e] = s #b가 속한 집합의 최상위 부모를 a로 설정
    else:
        parent[s] = e

parent = [i for i in range(V+1)]
edges.sort()
result = 0

for w,s,e in edges:
    if f_parent(s) != f_parent(e):
        mix_parent(s,e)
        result += w

print(result)