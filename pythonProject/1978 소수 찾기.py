from math import sqrt
# n = int(input())

# a = list(map(int,input().split()))

#어떤 수 x에 대해서 소수 판별을 하기 위해선, 2부터 x/2까지의 정수로 x가 나누어 떨어지는지를 판단하면 된다.
'''
# n = 4
# def is_prime(n):
#     flag = False #소수일지 모름디
# 
#     for i in range(2,n):
#         if n % i == 0:
#             flag = True
#             # print('얘는 합성수')
#             break
# 
#         # else:
#             # print('소수 필난다.')
#     return flag
# 
# if is_prime(n):
#     print('합성수')
# else:
#     print('소수')
'''
# n에 어떠한 값을 집어넣었을때 그 n이 소수인지 합성수인지 알려주는 함수.
# n이 n-1번까지 실행이 됬을때 전부 소수 필난다가 나오면 얘는 소수.

n = int(input())

a = list(map(int,input().split()))

cnt = 0
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

for num in a:
    if is_prime(num):
        cnt += 1
print(f'{cnt}')