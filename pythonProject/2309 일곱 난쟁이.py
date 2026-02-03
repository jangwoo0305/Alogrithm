# 아홉난쟁이의 키가 들어갈 배열을 생성
#
# 숫자 아홉개중 7개를 더해서 100을 만들어야하고 일곱난쟁이의 키는 오름차순으로 출력
# 9명 중에서 2명을 뺏더니 7명의 합이 100이다? 이걸로 하면 되지 않을까
# 9명의 키를 배열에 넣고 임의의 두개를 7개가 100이 될 때까지 뺀다.


import sys

heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline()))

total = sum(heights)
one = 0
two = 0

for i in range(9):
    for j in range(i+1, 9):
        if total - (heights[i] + heights[j]) == 100:
            one = heights[i]
            two = heights[j]
            break

heights.remove(one)
heights.remove(two)
heights.sort()

for i in heights:
    print(i)
