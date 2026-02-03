N = int(input())
integer = list(map(int,input().split()))
V = int(input())

count = 0

for i in integer:
    if i == V:
        count += 1

print(count)
    
