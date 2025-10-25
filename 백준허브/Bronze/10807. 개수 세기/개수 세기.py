N = int(input())
number_list = list(map(int,input().split()))
v = int(input())

total = 0

for i in range(N):
    if number_list[i] == v:
        total += 1

print(total)