import sys
input = sys.stdin.readline
N = int(input())
board =[]

for _ in range(N):
    board.append(list(map(int,input().split())))

dp = [[0]*N for _ in range(N)]

dp[0][0] = 1

