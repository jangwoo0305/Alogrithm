N,M = map(int,input().split())
number_list = list(map(int,input().split()))

for i in range(N):
    if number_list[i] < M:
        print(number_list[i],end =" ")