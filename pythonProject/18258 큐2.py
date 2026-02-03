import sys
input= sys.stdin.readline
queue = []
n = int(input())

for i in range(n):
    com = input().strip().split()

    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif com[0] =='size':
        print(len(queue))
    elif com[0] == 'empty':
        print(0 if queue else 1)
    elif com[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)