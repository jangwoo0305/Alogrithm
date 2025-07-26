N,M = map(int,input().split())
result = list(range(1,N+1))

for _ in range(M):
    i,j = map(int,input().split())
    result[i-1],result[j-1] = result[j-1],result[i-1]
    
print(*result)
