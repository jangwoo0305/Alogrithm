def upsidedown(N):
    ori = list(N)
    rev_list = list(N)
    rev_list.reverse()
    
    if ori == rev_list:
        print(1)
    else:
        print(0)
        

if __name__ == "__main__":
    N = input()
    upsidedown(N)

