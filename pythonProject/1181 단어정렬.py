import sys

n = int(sys.stdin.readline().rstrip())
ls = []

for _ in range(n):
    ls.append(sys.stdin.readline().strip())

set_ls = set(ls)
ls = list(set_ls)
ls.sort()
ls.sort(key = len)

for i in ls:
    print(i)

#set 내장함수
# [집합]
# 순서가 없다(인덱스로 접근하지 못한다.)
# 중복은 허용되지 않는다.
# 요소는 변경 불가능한 자료형만 사용할 수 있다.










