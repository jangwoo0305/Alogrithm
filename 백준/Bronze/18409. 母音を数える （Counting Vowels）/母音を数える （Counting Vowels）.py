N = int(input())
S = input()

total = 0

for i in S:
    if i in ['a','i','u','e','o']:
        total += 1

print(total)
