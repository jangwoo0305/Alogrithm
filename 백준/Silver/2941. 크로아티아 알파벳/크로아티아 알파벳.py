def croatia(N):
    cro = ['dz=','c=','c-','d-','lj','nj','s=','z=']

    for c in cro:
        N = N.replace(c,'*')

    print(len(N))


if __name__ == '__main__':
    N = input()
    croatia(N)