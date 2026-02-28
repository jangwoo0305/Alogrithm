def _Factor(A,B):
    if B % A == 0:
        print('factor')
    elif A % B == 0:
        print('multiple')
    else:
        print('neither')



if __name__ == "__main__":
    while True:
        A,B= map(int,input().split())
        if A == 0 or B == 0:
            break
        _Factor(A,B)

