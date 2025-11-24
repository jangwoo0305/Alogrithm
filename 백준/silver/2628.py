x,y = map(int,input().split())

wid = [x,0] # 가로
length = [0,y] # 세로

Cut_Time = int(input())
for i in range(Cut_Time):
    N,M = map(int,input().split())
    if N == 0:
        length.append(M)
    else:
        wid.append(M)
        
wid.sort()
length.sort()

max_w = 0
for i in range(1,len(wid)):
    max_w = max(max_w, wid[i]- wid[i-1])

max_l = 0
for i in range(1,len(length)):
    max_l = max(max_l, length[i] - length[i-1])
    
print(max_w * max_l)