a = list() #a라는 이름의 list를 만든다.

def solve(a): #백준에서 사용하라던 코드
    sum = 0     # 수를 더하는 변수를 sum이라 선언하고 0으로 초기값을 해놓는다.
    for num in a:  #a 리스트안의 요소를 num으로 계속 실행
        sum += num  #sum과 num더한다,
    return sum #sum의 결과를 반환한다.



