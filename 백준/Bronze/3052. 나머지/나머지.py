value_array = []

def remain_num():
    for _ in range(10):
        N = int(input())
        A = N % 42
        if len(value_array) == 0:
            value_array.append(A)
        for I in range(len(value_array)):
            if value_array[I] == A:
                break
            elif I == len(value_array)-1:
                value_array.append(A)

    return len(value_array)

if __name__ == "__main__":
    remain_num()
    print(len(value_array))
