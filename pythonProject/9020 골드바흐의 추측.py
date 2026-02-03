# 2보다 큰 짝수는 두개의 소수의 합으로 나타낼 수 있다.
# num을 어떠한 짝수라고 하고 p1과 p2를 소수라고 한다.
# num - p1 = p2 / p1 + p2 = num
# 소수에서 소수의 차가 가장 작은 것을 출력한다.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True


n = int(input())
for i in range(n):
    num = int(input())

    a , b = num//2 ,num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        else:
            a -= 1
            b += 1
