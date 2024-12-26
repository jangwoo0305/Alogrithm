age, gender = input().split()
age1, gender1 = input().split()
age = int(age)
age1 = int(age1)

if age >= 19 or age1 >= 19:
    if gender == "M" or gender1 == "M":
        print(1)
    else:
        print(0)

