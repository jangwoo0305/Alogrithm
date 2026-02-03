# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# arr = [] # 입력된 정수 저장
# while True:
#     try:
#         x = int(input())
#         arr.append(x)
#     except:
#         break
#
# def sol(A):
#     if len(A) == 0:
#         return
#
#     Left, Right = [], []
#     root = A[0]
#     for i in range(1, len(A)):
#         if A[i] > root:
#             Left = A[1:i]
#             Right = A[i:]
#             break
#     else:
#         Left = A[1:]
#
#     sol(Left)
#     sol(Right)
#     print(root)
#
# sol(arr)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

arr = []  # 입력된 정수 저장
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def sol(A): #A에는 예제 입력값이 담긴다.
    if not A:
        return

    root = A[0]
    left = []
    right = []

    # A[1:] 부분에서 루트보다 작은 값들은 왼쪽 서브트리에, 큰 값들은 오른쪽 서브트리에 추가
    for value in A[1:]:
        if value < root:
            left.append(value)
        else:
            right.append(value)

    # 왼쪽 서브트리와 오른쪽 서브트리에 대해 재귀적으로 후위 순회 수행
    sol(left)
    sol(right)

    # 루트 출력
    print(root)

# 함수 호출
sol(arr)