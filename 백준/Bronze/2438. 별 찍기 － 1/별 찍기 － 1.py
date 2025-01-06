N = int(input())

for i in range(N): # 이 반복문이 한번 돌때마다 행이 바뀐다.
    for _ in range(i+1):
        print("*", end="")
    print()        