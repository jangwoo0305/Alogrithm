import sys
input = sys.stdin.readline

N , K = map(int,input().split())

def solve(N, K):
    people = list(range(1, N + 1))
    result = []
    index = 0

    while people:
        index = (index + K - 1) % len(people)
        result.append(people.pop(index))

    return result

result = solve(N, K)
print("<",",".join(map(str,result)), ">",sep="")

