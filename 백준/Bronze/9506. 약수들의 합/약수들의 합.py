def Factors_sum(N):
    factor = []
    for i in range(1,N):
        if N % i == 0:
            factor.append(i)

    if sum(factor) == N:
        result = " + ".join(map(str, factor))
        print(f"{N} = {result}")
    else:
        print(f"{N} is NOT perfect.")


if __name__ == "__main__":

    while True:
        N = int(input())
        if N == -1:
            break

        Factors_sum(N)
