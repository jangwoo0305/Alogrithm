import sys
input = sys.stdin.readline

stair_num = int(input())

points = [0]
for _ in range(stair_num):
    points.append(int(input()))

if stair_num == 1:
    print(points[1])
elif stair_num == 2:
    print(points[1] + points[2])
else:
    dp = [0] * (stair_num+1)

    dp[1] = points[1]
    dp[2] = points[1] + points[2]

    for cur_stair in range(3 , stair_num + 1):
        dp[cur_stair] = max(dp[cur_stair - 2] + points[cur_stair],
                             dp[cur_stair-3] + points[cur_stair-1] + points[cur_stair])


    print(dp[stair_num])