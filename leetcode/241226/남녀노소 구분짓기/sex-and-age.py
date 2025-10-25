gender = int(input())
age = int(input())


print(("MAN" if age >= 19 else "BOY")if gender == 0 else ("WOMAN" if age >= 19 else "GIRL"))