# 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족시키지 못함
# 즉, 가장 긴 변을 제외한 나머지 두변의 길이의 합이 가장 긴 변의 길이 보다 길어야 함
def make_Rec(side):
    side.sort() # 오름차순 정렬

    if side[2] >= side[0] + side[1]:
        side[2] = side[0] + side[1] - 1

    return sum(side)



if __name__ == "__main__":

    side = list(map(int,input().split()))
    print(make_Rec(side))