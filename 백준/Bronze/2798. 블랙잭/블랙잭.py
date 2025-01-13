N,M = map(int,input().split())
card_list = list(map(int,input().split()))
card_sum = []

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            card_sum.append(card_list[i] + card_list[j] + card_list[k])
            
result = 0
for s in card_sum:
    if s <= M and s > result:
        result = s

print(result)
