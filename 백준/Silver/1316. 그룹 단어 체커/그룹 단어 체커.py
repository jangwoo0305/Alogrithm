def Group_Word(N):
    count = 0

    for _ in range(N):
        word = list(input())
        prev = ' '
        used = set()

        for i in word:
            if i != prev:
                if i in used:
                    break
                used.add(i)
            prev = i
        else:
            count += 1

    print(count)



if __name__ == "__main__":
    N = int(input())
    Group_Word(N)



