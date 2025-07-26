N,M = map(int,input().split())

result = [0] * N

for x in range(M):
    i,j,k = map(int,input().split())
    for idx in range(i-1,j):
        result[idx] = k

print(*result)