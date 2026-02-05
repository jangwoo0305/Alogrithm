def ball_put():
    N, M = map(int, input().split())
    
    basket = []
    for i in range(N+1):
        basket.append(i)

    for _ in range(M):
        i,j = map(int, input().split())
        basket[i],basket[j] = basket[j],basket[i]

    for i in range(1,N+1):
        print(basket[i], end = ' ')


if __name__ == "__main__":
    ball_put()