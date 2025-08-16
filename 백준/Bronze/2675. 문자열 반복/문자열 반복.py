S = int(input())

for _ in range(S):
    R, S = input().split()
    R = int(R)
    result = ""
    for char in S:
        result += char * R
    print(result)