A = list(map(int,input().split()))

total = 0

for i in A:
    total += i*i
print(total % 10)