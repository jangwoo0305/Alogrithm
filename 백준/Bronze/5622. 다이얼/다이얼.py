def dial(N):
    count = 0

    for i in N:
        if 'A' <= i <= 'C':
            count += 3
        elif 'D' <= i <= 'F':
            count += 4
        elif 'G' <= i <= 'I':
            count += 5
        elif 'J' <= i <= 'L':
            count += 6
        elif 'M' <= i <= 'O':
            count += 7
        elif 'P' <= i <= 'S':
            count += 8
        elif 'T' <= i <= 'V':
            count += 9
        elif 'W' <= i <= 'Z':
            count += 10
        else:
            count += 11

    print(count)


if __name__ == '__main__':
    N = list(input())
    dial(N)
