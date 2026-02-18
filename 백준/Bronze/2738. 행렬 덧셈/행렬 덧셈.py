def Graduation(A,B):
    N = len(A) ## 행의 갯수
    M = len(A[0]) ## 열의 갯수

    for i in range(N):
        for j in range(M):
            print(A[i][j] + B[i][j], end=" ")
        print()


if __name__ == "__main__":
    N,M = map(int,input().split())

    A = []
    for _ in range(N):
        A.append(list(map(int,input().split())))

    B = []
    for _ in range(N):
        B.append(list(map(int,input().split())))

    Graduation(A,B)
