N,M = map(str,input().split())

A = N[::-1]
B = M[::-1]

if(int(A)>int(B)):
    print(int(A))
else:
    print(int(B))