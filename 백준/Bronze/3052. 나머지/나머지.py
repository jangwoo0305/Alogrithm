total = []

for i in range(10):
    N = int(input())
    if N % 42 not in total:
        total.append(N%42)

print(len(total))
