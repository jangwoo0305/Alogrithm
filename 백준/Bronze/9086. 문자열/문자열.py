def print_word():
    T = int(input())

    for _ in range(T):
        N = input()
        print(N[0] + N[-1])

if __name__ == "__main__":
    print_word()
