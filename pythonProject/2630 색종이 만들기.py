import sys

n = int(sys.stdin.readline())
papercolor = []

for i in range(n):
    papercolor.append(list(map(int, sys.stdin.readline().split())))

blue = 0
white = 0

def fold(minx, maxx, miny, maxy):
    global blue
    global white

    isblue = True
    iswhite = True

    for i in range(minx,maxx):
        for j in range(miny, maxy):
            if papercolor[i][j] == 0:
                isblue = False
            if papercolor[i][j] == 1:
                iswhite = False

    if isblue:
        blue += 1
    elif iswhite:
        white += 1
    else:
        midx = (minx + maxx) // 2
        midy = (miny + maxy) // 2
        fold(minx,midx,miny,midy)
        fold(midx,maxx,miny,midy)
        fold(minx,midx,midy,maxy)
        fold(midx,maxx,midy,maxy)

fold(0, n, 0, n)
print(white)
print(blue)