def zigzag(N): # N = 8
    layer = 0  # 4
    last_num = 0 # 10

    while N > last_num:
        layer += 1
        last_num += layer

    offset = last_num - N

    if layer % 2 == 0:
        top = layer - offset
        bottom = offset + 1
    else:
        top = offset + 1
        bottom = layer - offset

    print(f"{top}/{bottom}")




if __name__ == "__main__":
    N = int(input())
    zigzag(N)
