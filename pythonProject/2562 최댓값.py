# number = list(map(int,input().split()))
# position = 7 + 1
# print(number[7])
# print(position)

# 숫자1 을 숫자2와 비교해 큰 숫자와 몇번째인지 기억해둔다.
# 둘중 큰 숫자를 숫자3과 비교해 큰 숫자와 몇번째인지 기억해둔다.
# 숫자 9까지 반복한다.
# 가장 큰 숫자와 몇번째인지 출력한다.


a = list() # 리스트를 만든다.

for i in range(9): #리스트의 크기는 0~8까지 총 9칸
    a.append(int(input())) #append를 사용하용하여 리스트에 요소를 추가한다.

max = a[0] #리스트의 첫번째 요소를 가장 큰 최댓값으로 설정해 놓는다.
for i in a: #
    if max<i:
        max = i
print(max)
print((a.index(max))+1)


a = list() # 리스트를 만든다.

for i in range(9): #리스트의 크기는 0~8까지 총 9칸
    a.append(input()) #위의 코드와 다르게 int를 제거하여 문자를 입력하게 되면 아스키코드의 최댓값을 가지고 있는 문자가 출력되게 된다.

max = a[0] #리스트의 첫번째 요소를 가장 큰 최댓값으로 설정해 놓는다.
for i in a: #
    if max<i:
        max = i
print(max)
print((a.index(max))+1)




