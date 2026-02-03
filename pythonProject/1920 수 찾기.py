n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

for m in m_list:
    pl = 0
    pr = n - 1

    while pl <= pr:
        mid = (pl + pr)//2
        if m > n_list[mid]:
            pl = mid + 1
        elif m <n_list[mid]:
            pr = mid - 1
        else:
            pl = mid
            pr = mid
            break

    if pl == mid and pr == mid:
        print(1)
    else:
        print(0)


