N = int(input())

meeting_time = []

for i in range(N):
    S,E = map(int,input().split())
    meeting_time.append((S,E))
    
meeting_time.sort(key = lambda x : (x[1],x[0]))

end = meeting_time[0][1]# 4
count = 1
for i in range(1,N):
    if meeting_time[i][0]>=end:
        end = meeting_time[i][1]
        count += 1
        
print(count)