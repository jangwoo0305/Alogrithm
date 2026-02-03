# n = int(input())
#
# for i in range(n):
#     repeat_count, char = input().split()
#     repeat_count = int(repeat_count)
#
#     result = ''
#         for c in char:
#             result += c * repeat_count
#
# print(result)

n = int(input())

# 결과를 저장할 변수를 초기화합니다.
result = ''

for i in range(n):
    repeat_count, char = input().split()
    repeat_count = int(repeat_count)

    # 각 문자열을 repeat_count 만큼 반복하여 결과에 추가합니다.
    for c in char:
        result += c * repeat_count

# 모든 반복이 끝난 후에 결과를 출력합니다.
print(result)
