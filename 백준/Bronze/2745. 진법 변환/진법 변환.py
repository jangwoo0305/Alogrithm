def Change(N,B):
    result = 0
    for ch in N:
        if '0' <= ch <= '9':
            value = int(ch)
        else:
            value = ord(ch) - 55

        result = result * B + value

    print(result)



if __name__ == "__main__":
    N,B = input().split()
    B = int(B)

    Change(N,B)


