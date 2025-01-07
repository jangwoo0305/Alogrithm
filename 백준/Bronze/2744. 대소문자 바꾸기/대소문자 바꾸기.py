N = input()

for i in N:
    if i.isupper() == True:
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")