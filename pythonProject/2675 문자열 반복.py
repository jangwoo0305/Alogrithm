# 사용자로부터 문자 입력받기
# char = input("문자를 입력하세요: ")

# 출력할 횟수 입력받기
# repeat_count = int(input("출력할 횟수를 입력하세요: "))

# 문자를 반복해서 출력하기
# result = char * repeat_count

# 결과 출력하기
# print(result)

# repeat_count = int(input())
#
# char = input()
#
# result = char * repeat_count
#
# print(f'{repeat_count}  {result}')

n = int(input()) #  사용자로부터 정수값은 입력받고 이 값은 반복 횟수를 나타낸다.

for i in range(n):  #입력받은 정수 n만큼 반복
    repeat_count, char = input().split() #사용자로부터 입력을 받고, 입력값을 공백을 기준으로 나누어 repeat_count와 char 변수에 할당.
    repeat_count = int(repeat_count)    #repeat_count 변수에 할당된 값을 정수로 변환. 문자열 형태의 숫자를 정수로 변환하여 반복 횟수로 사용.

    result = ''.join([char * repeat_count for char in char])
    #리스트 컴프리헨션을 사용하여 'char' 문자열의 각 문자를 순회하며, 'char * repeat_count'를 계산.

    #각 'char' 문자는 'repeat_count'만큼 반복된다.
    print(result)

    # result = char * repeat_count
    # #리스트가 되 문자열의 각 요소를 repeat_count만큼 곱한다.
    #
    # print(f'{repeat_count} {result}')
