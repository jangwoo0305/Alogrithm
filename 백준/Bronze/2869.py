A,B,V = map(int,input().split())

# day = 0
# upmeter = 0

# for i in range(V):
#     C = A - B
#     upmeter += C
#     if upmeter >= V:
#         print(day)
#         break
#     else:
#         day += 1

if (V-B)%(A-B) == 0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B)+1)
