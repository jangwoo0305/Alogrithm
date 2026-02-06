def New_AVG():
    N = int(input())
    point = list(map(int, input().split()))

    C = max(point)

    total = 0
    for P in point:
        total += P / C * 100

    print(total/N)



if __name__ == "__main__":
    New_AVG()