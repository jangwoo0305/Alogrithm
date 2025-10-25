n = int(input())  # 사용자로부터 숫자 입력 받음
star = ""  # 빈 문자열로 초기화

for i in range(n):
    star += "*"  # 별 하나 추가
    print(star)  # 현재 문자열 출력


# N = int(input())

# for i in range(N): # 이 반복문이 한번 돌때마다 행이 바뀐다.
#     for _ in range(i+1):
#         print("*", end="")
#     print()      
