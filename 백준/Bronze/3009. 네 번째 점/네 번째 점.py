def find_loc(point):
    x_list = []
    y_list = []

    for x,y in point:
        x_list.append(x)
        y_list.append(y)

    for x in x_list:
        if x_list.count(x) == 1:
            x_result = x

    for y in y_list:
        if y_list.count(y) == 1:
            y_result = y

    return x_result,y_result

if __name__ == "__main__":

    point = []

    for _ in range(3):
        x,y = map(int,input().split())
        point.append((x,y))

    x,y = find_loc(point)
    print(x,y)