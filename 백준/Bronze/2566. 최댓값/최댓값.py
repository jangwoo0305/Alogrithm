def max_value(A):
    max_val = 0
    max_row = 0
    max_col = 0

    for i in range(9):
        for j in range(9):
            if A[i][j] > max_val:
                max_val = A[i][j]
                max_row = i
                max_col = j

    print(max_val)
    print(max_row+1, max_col+1)



if __name__ == '__main__':
    A = []
    for _ in range(9):
        row = list(map(int, input().split()))
        A.append(row)
    max_value(A)
