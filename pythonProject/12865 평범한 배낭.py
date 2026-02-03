# import sys
# input = sys.stdin.readline
# stuff = [[0.0]] #물건의 무게와 가치를 저장해 놓는 리스트.
# things_num ,total_Weight = map(int,input().split())
#
# dp = [[0]*(total_Weight+1) for _ in range(things_num+1)]
#
# for _ in range(things_num):
#     stuff.append(list(map(int,input().split())))
#
# for i in range(1, things_num+1):
#     for j in range(1,total_Weight+1):
#         temp_weight = stuff[i][0]
#         temp_value = stuff[i][1]
#
#         if j < temp_weight:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(temp_value + dp[i-1][j-temp_weight],dp[i-1][j])
#
# print(dp[things_num][total_Weight])
#
#
import sys

N , K = map(int,sys.stdin.readline().split())
object_list = []

for _ in range(N):
    w , v = map(int,sys.stdin.readline().split())
    object_list.append((w , v))

dp = [[0 for i in range(K+1)] for j in range(N+1)]

for idx in range(1,N+1):
    cur_weight , cur_val = object_list[idx-1]
    for max_weight in range(1,K+1):
        if max_weight < cur_weight:
            dp[idx][max_weight] = dp[idx-1][max_weight]
        else:
            dp[idx][max_weight] = max(dp[idx-1][max_weight],dp[idx-1][max_weight - cur_weight] + cur_val)

print(dp[-1][-1])