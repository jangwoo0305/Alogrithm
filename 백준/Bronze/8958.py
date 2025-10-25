N = int(input())


for i in range(N):
    M = input()
    point = 0
    sum_point = 0   
    
    for j in M:
        if j == 'O':
            point += 1
        else:
            point = 0
        sum_point += point
    print(sum_point)
    