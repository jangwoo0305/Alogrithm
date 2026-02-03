# 숫자를 입력하면 하나씩 빼면서 전부 곱한다.
#
# 10을 입력하면 하나가 빠진 9를 출력해 곱하고 그 값에 8을 곱하고 하는 식으로 -1씩 빼면서 1까지 곱한다

num = int(input())

def fac(num):
    if num > 1:
        return num * fac(num - 1)
    else:
        return 1

print(fac(num))