def fire(N,M):
    student_count = {}

    for _ in range(N):
        K = int(input())
        student_ids = list(map(int, input().split()))

        for i in student_ids:
            if i in student_count:
                student_count[i] += 1
            else:
                student_count[i] = 1

    total_count = 0
    for count in student_count.values():
        if count >= M:
            total_count += 1
    print(total_count)


if __name__ == "__main__":
    N, M = map(int, input().split())
    fire(N, M)


