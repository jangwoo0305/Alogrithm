def Prime_fac(N):
    div = 2

    if N == 1:
        return

    while N > 1:
        if N % div == 0:
            print(div)
            N //= div
        else:
            div += 1




if __name__ == "__main__":
    N = int(input())
    Prime_fac(N)


