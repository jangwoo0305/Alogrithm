def Change(N,B):
    result = []
    while N > 0:
        rest = N % B
        result.append(rest)
        N = N // B

    result.reverse()
    answer = ""
    for i in result:
        if i < 10:
            answer += str(i)
        else:
            answer += chr(i + 55)
    print(answer)


if __name__ == "__main__":
    N,B = map(int,input().split())
    Change(N,B)

