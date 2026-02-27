def Bee_house(N):
    layer = 1   # 1, 2,  3,  4,  5
    max_num = 1 # 1, 7, 19, 37, 61
    
    while (max_num < N):
        max_num += 6 * layer
        layer += 1

    print(layer)

if __name__ == "__main__":
    N = int(input())
    Bee_house(N)


--------------------------------
# 처음 제출한 코드
def Bee_house(N):
    layer = 1   # 1, 2,  3,  4,  5
    max_num = 1 # 1, 7, 19, 37, 61

    if N == 1:
        print(1)

    while (max_num < N):
        max_num = 6 * layer + max_num
        layer += 1
        if max_num >= N:
            print(layer)



