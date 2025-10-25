N = int(input())
num_list = list(map(int,input().split()))

total = 0

for i in num_list:
    for j in range(2,i+1):
        if i % j == 0:
            if i == j:
                total += 1
            break

print(total)
