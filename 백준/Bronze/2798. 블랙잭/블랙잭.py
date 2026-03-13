def BlackJack(N,M,card):
    result = 0 # 가까운 값을 찾기 위해서 만든 변수

    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                sum_card = card[i] + card[j] + card[k]

                if sum_card <= M and sum_card > result:
                    result = sum_card
    return result


if __name__ == "__main__":

    N,M = map(int,input().split())
    card = list(map(int,input().split()))
    print(BlackJack(N,M,card))