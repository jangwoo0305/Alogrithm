n = int(input())
li = []

for i in range(n):
    li.append(int(input()))

for i in range (len(li)):

    for j in range(len(li)):

        if li[i] > li[j]:
            li[i] , li[j] = li[j], li[i]

        return
#

# data = [5, 2, 4, 3, 1]
#
# dataNum = len(data)
# # 회차별 반복문
# for i in range(dataNum-1):
#     # 각 회차에서 원소를 비교하는 반복문
#     for j in range(dataNum - i - 1):
#         if data[j] > data[j+1]:
#             data[j], data[j+1] = data[j+1], data[j]
#         print(i+1, '회차', data)
#     # print(i+1, '회차결과', data)


def bubble(num) :
    for i in range(len(num)) :
        for j in range(len(num)) :
            if num[i] < num[j] :
                num[i], num[j] = num[j], num[i]
    return num


n = int(input())
num = []

for _ in range(n) :
    num.append(int(input()))

number = bubble(num)
for i in number :
    print(i)
