def Paper(white,X,Y):
    for i in range(X, X + 10):
        for j in range(Y, Y + 10):
            white[i][j] = 1

def Area(white):
    area = 0
    for i in range(100):
        for j in range(100):
            if white[i][j] == 1:
                area += 1
    return area

if __name__ == "__main__":

    white = [] # 하얀색 종이 공간
    for i in range(100):
        row = []
        for j in range(100):
            row.append(0)
        white.append(row)

    N = int(input())
    for _ in range(N):
        X,Y = map(int,input().split())
        Paper(white,X,Y)

    area = Area(white)
    print(area)
