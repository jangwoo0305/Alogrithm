N = int(input())
A_list = list(map(int,input().split()))

count = 0

for i in A_list:
    for j in range(2,i+1):
        if i % j == 0:
            if i == j:
                count += 1

print(count)