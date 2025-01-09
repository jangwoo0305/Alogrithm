N_list  = list(map(int,input().split()))

if N_list == sorted(N_list):
    print("ascending")
elif N_list == sorted(N_list,reverse=True):
    print("descending")
else:
    print("mixed")