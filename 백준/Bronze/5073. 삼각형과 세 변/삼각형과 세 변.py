# 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족시키지 못함
# 즉, 가장 긴 변을 제외한 나머지 두변의 길이의 합이 가장 긴 변의 길이 보다 길어야 함
def find_Rec(Rec):
    if max(Rec) >= sum(Rec)-max(Rec):
        return "Invalid"

    if Rec[0] == Rec[1] == Rec[2]:
        return "Equilateral"
    elif Rec[0] == Rec[1] or Rec[0] == Rec[2] or Rec[1] == Rec[2]:
        return "Isosceles"
    else:
        return "Scalene"

if __name__ == "__main__":
    while True:
        Rec = list(map(int,input().split()))
        if Rec == [0,0,0]:
            break

        print(find_Rec(Rec))