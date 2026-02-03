import sys
input = sys.stdin.readline

N , K = map(int,input().split()) # N : 화폐 종류 수, K : 거슬러 줄 돈

coins = []
for _ in range(N):
    coins.append(int(input()))

