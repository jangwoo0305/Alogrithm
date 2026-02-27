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
