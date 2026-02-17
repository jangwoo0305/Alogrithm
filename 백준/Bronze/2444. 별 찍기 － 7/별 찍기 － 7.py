def print_Star(N):
    for i in range(N):
        space = N - 1 - i
        star = 2 * i + 1
        print(' ' * space + '*' * star)

    for i in range(N-2,-1,-1):
        space = N - 1 - i
        star = 2 * i + 1
        print(' ' * space + '*' * star)


if __name__ == "__main__":
    N = int(input())
    print_Star(N)


