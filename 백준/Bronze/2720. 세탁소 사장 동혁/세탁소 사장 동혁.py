def Laundry(C):

    sample = [25,10,5,1]
    count = []

    for i in range(4):
        A = C // int(sample[i])
        count.append(A)
        B = C % int(sample[i])
        C = B

    print(*count)

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        C = int(input())
        Laundry(C)


