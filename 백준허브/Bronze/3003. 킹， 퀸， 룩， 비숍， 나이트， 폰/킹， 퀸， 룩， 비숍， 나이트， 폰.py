N_list = [1,1,2,2,2,8]
A = list(map(int,input().split()))

for i in range(6):  
    print(N_list[i]-A[i],end=" ")