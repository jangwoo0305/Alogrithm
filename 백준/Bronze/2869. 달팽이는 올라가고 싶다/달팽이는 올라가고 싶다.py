# def snail(A,B,V):
#     current_height = 0
#     day = 0
#
#     while current_height <= V:
#         current_height += A
#
#         if current_height > V:
#             break
#         current_height -= B
#         day += 1
#
#     print(day)

def snail(A,B,V):
    if (V-B)%(A-B) == 0:
        print((V-B)//(A-B))
    else:
        print((V-B)//(A-B)+1)




if __name__ == "__main__":
    A,B,V = map(int,input().split())
    snail(A,B,V)

