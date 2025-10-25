N = int(input())
T_list = list(map(int,input().split()))
T,P = map(int,input().split())

t_number = 0

for i in T_list:
    if i == 0:
        continue
    elif i <= T:
        t_number += 1
    else:
        if i % T == 0:
            t_number += i // T  
        else:
            t_number += i // T + 1  
        
            

p_bundle = N//P
pen = N%P
        
    
print(t_number)
print(p_bundle,pen)