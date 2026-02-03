import sys

n = int(input())
li = []

for _ in range (n):
    li.append(int(sys.stdin.readline().rstrip()))

li.sort()

for num in li:
    print(num)