N = int(input())
floor = 1
cnt = 1

while N > floor:
    floor += 6 * cnt
    cnt += 1

print(cnt)