# 소수 : 1이랑 자기 자신만을 약수로 가지는 수
def decimal(M,N):
    dec = []
    for i in range(M,N+1):
        if i == 1:
            continue
        for x in range(2,i):
            if i % x == 0:
                break
        else:
            dec.append(i)
    if len(dec)==0:
        print(-1)
    else:
        print(sum(dec))
        print(min(dec))



if __name__ == "__main__":
    M = int(input())
    N = int(input())
    decimal(M,N)


