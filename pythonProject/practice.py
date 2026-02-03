# 3정수의 중간값을 찾기
# def med3(a,b,c):
#     # if a >= b:
#     #     if a <= c:
#     #         return a
#     #     elif b >= c:
#     #         return b
#     #     else :
#     #         return c
#     # else :
#     #     if a <= b:
#     #         if b <= c:
#     #             return b
#     #         elif a >= c:
#     #             return a
#     #         else :
#     #             return c
#
#     if (b<=a<=c) or (c<=a<=b):
#         return a
#     elif (c<=b<=a) or (a<=b<=c):
#         return b
#     else:
#         return c
#
# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수a의 값을 입력하시오:'))
# b = int(input('정수b의 값을 입력하시오:'))
# c = int(input('정수c의 값을 입력하시오:'))
#
# print(f'중간값은 {med3(a,b,c)}입니다')
#
# 실습1-3
# n = int(input())
# if n > 0:
#     print('이 수는 양수입니다')
# elif n < 0:
#     print('이 수는 음수입니다')
# else:
#     print('이 수는 0입니다')
#
# 실습 1-7
# print('1부터 n까지의 정수의 합을 구합니다.')
# n = int(input('n의 값을 입력하시오. :'))
#
# sum = 0
# i = 1
#
# while i <= n:
#     sum += i
#     i += 1
# print(f'1부터 {n}까지의 정수의 합은 {sum}입니다.')
# print(f'i값은 {i}입니다.')

# #실습 1-8
# print('1부터 n까지의 정수의 합을 구합니다.')
# n = int(input('n값을 입력하시오.:'))
#
# sum = 0
# for i in range(1, 1 + n):
#     sum += i
# print({f'1부터 {n}까지의 정수의 합은 {sum}입니다'})
# print(f'i값은 {i}입니다.')

# #실습 1-9
# print('a부터 b까지의 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.:'))
# b = int(input('정수 b를 입력하세요.:'))
#
# if a > b:
#     a, b = b, a # a와 b의 값을 교환
#
# sum = 0
# for i in range(a, b + 1):
#     sum += i
# print(f'{a}부터 {b}까지의 정수의 합은 {sum}입니다')

# #실습 1-10
# print('a부터 b까지의 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.:'))
# b = int(input('정수 b를 입력하세요.:'))
# if a > b:
#     a,b = b,a
#
# sum = 0
# for i in range(a, b+1):
#     if i < b:
#         print(f'{i} + ', end='')
#     else:
#         print(f'{i} = ', end='')
#     sum += i
# print(sum)

# # 실습 1- 11
# print('a부터 b까지의 정수의 합을 구합니다.')
# a = int(input('정수 a를 입력하세요.:'))
# b = int(input('정수 b를 입력하세요.:'))
# if a > b:
#     a,b = b,a
#
# sum = 0
# for i in range(a, b):
#     print(f'{i} + ', end='')
#     sum += i
#
# print(f'{b} = ', end='')
# sum += b
#
# print(sum)

# # 실습 1-12
# print('+와 -를 번갈아 출력합니다')
# n = int(input('몇개를 출력할까요?'))
#
# for i in range(n):
#     if i % 2: #조건식 해석 'i"가 홀수를 의미
#         print('-',end='')
#     else:
#         print('+', end='')
# print()

#위의 코드는 0부터 n-1까지로 짝수인 0이 먼저 실행되므로 else구문부터 시작하는 반면
#아래의 코드는 1부터 n+1까지로 홀수인 1이 먼저 실행되므로 if구문이 먼저 진행되기 때문에 홀수 일때 -였던 부분을 홀수일때 +로 바꿔줘야
#위와 아래의 코드가 같은 결과값을 도출한다.

# print('+와 -를 번갈아 출력합니다')
# n = int(input('몇개를 출력할까요?'))
#
# for i in range(1, n + 1):
#     if i % 2:
#         print('+',end='')
#     else:
#         print('-', end='')
# print()

# if (조건?):
#     ??
#     변수 -> bool -> True or False
#     Ture False
#     정수 -> bool -> 0 -> 0 -> False 나머지 -> 1 -> True
#     변수가 -1이면? ->
#
#
# if (변수) :

# #실습 1-13
# print('+와 -를 번갈아 출력합니다')
# n = int(input('몇개를 출력할까요?'))
#
# for _ in range(n//2): #실수형의 숫자가 나오면 뒤에 소수점 부분을 제하고 정수형 부분만 가져온다.
# 0이상 2미만 증감1 ->0과1 2번
#     # i -> index -> 순번
#     print('+-', end='')

# if n % 2: #n이 홀수
#     print('+',end='')
#
# print()

#실습 1-13-1
# print('+와 -를 번갈아 출력합니다')
# n = int(input('몇개를 출력할까요?'))
#
# for _ in range(1, n//2+1): #2+1을 먼저 해서 n//3이 되는게 아니라 n//2를 하고 +1을 해서 3이 된다.
#     #-->for _ in range(1,3)이 되므로 1,2가 출력이 된다.
#     print('+-', end='')
#
# if n % 2: #n이 홀수
#     print('+',end='')
#
# print()

# #실습 1-14
# print('*를 출력합니다.')
# n = int(input('몇개를 출력할까요?'))
# w = int(input('몇개마다 줄바꿀까요?'))
#
# for i in range(n):
#     print('*',end='')
#     if i % w == w - 1:
#         print()
#
# if n % w:
#     print()

# #실습 1-15
# print('*를 출력합니다.')
# n = int(input('몇개를 출력할까요?'))
# w = int(input('몇개마다 줄바꿀까요?'))
#
# for _ in range(n//w):
#     print('*'* w)
#
# rest = n % w
# if rest:
#     print('*' * rest)

# #실습 1-16
# print('1부터 n까지 정수의 합을 구합닏다.')
#
# while True:
#     n = int(input('n의 값을 입력하세요.:'))
#     if n > 0:
#         break # n의 값이 0보다 클 경우 while문을 탈출하여 아래 코드로 진행
#
# sum = 0
# i = 1
#
# for i in range(1,n+1):
#     sum+=i
#     i +=1
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#실습 1-17?????????????????????????????????이해를 못하겠네 진짜
# area = int(input('직사각형의 넓이를 입력하세요.:'))
#
# for i in range(1, area + 1): #1~16
#     if i * i > area:
#         break #i=4 이상일때부터 break
#     if area % i:
#         continue
#     print(f'{i}*{area//i}')

#실습 1-21
# print('-' * 27)
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i*j:3}', end='') #:3은 너비를 뜻한다 한자리숫자라면 앞뒤로 공백이 하나씩 추가가 되지만 두자리 숫자라면 앞쪽에 공백이 하나 생긴다.
#     print()
# print('-' * 27)

#실습 1-22
# print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요.'))
#
# for i in range(n):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# #실습 1-23
# print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
# n = int(input('짧은 변의 길이를 입력하세요.'))
#
# for i in range(n):
#     for _ in range(n - i - 1): #ex) i = 0 이라면 n - 0 - 1 = 4 즉 4개의 공백이 출력
#         print(' ', end='')
#     for _ in range(i + 1): #ex) i = 0 이라면 0 + 1 = 1 즉 1개의 별이 출력
#         print('*', end='')
#     print()
#
# arr = [1,2,3]
# n = len(arr)
#
# print(n)


def dsf(v):
    visited[v] = True
    global cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dsf(i)


c = int(input())
L = int(input())

graph = [[] for _ in range(c+1)]

for i in range(L):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (c+1)
cnt = 0

dsf(1)
print(cnt-1)
