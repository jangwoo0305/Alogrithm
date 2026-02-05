def rev_basket():
    N,M = map(int,input().split())
    basket = []

    for i in range(N+1):
        basket.append(i)

    for _ in range(M):
        i,j = map(int,input().split())
        left = i
        right = j

        while left < right:
            basket[left], basket[right] = basket[right], basket[left]
            left += 1
            right -= 1

    for i in range(1,N+1):
        print(basket[i], end = ' ')


if __name__ == "__main__":
    rev_basket()