def add_int(N):
    hours = [4,6,4,10]
    work = {}

    for i in range(4 * N):
        names = input().split()
        time = hours[i % 4]

        for name in names:
            if name == '-':
                continue

            if name not in work:
                work[name] = 0
            work[name] += time

    if not work:
        return "Yes"

    value = work.values()
    if max(value) - min(value) <= 12:
        return "Yes"
    else:
        return "No"

def main():
    N = int(input())
    result = add_int(N)
    print(result)

if __name__ == "__main__":
    main()

