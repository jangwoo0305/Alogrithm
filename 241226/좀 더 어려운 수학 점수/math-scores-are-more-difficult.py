a,b = map(int,input().split())
c,d = map(int,input().split())

if a > c:
    print("A")
else:
    print("B")

if a == c:
    if b > d:
        print("A")
    else:
        print("B")