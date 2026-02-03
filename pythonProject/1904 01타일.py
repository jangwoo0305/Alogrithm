import sys
input = sys.stdin.readline

n = int(input().strip())

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    fib = [0] * (n+1)
    fib[1] = 1
    fib[2] = 2

    for i in range(3, n+1):
        fib[i] = (fib[i-1] + fib[i-2])%15746

    return fib[n]

print(fib(n))