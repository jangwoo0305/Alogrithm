def read_seok(A):
    for col in range(15):
        for row in range(5):
            if col < len(A[row]):
                print(A[row][col], end="")



if __name__ == '__main__':
    A = []
    for _ in range(5):
        row = input()
        A.append(row)
    read_seok(A)
