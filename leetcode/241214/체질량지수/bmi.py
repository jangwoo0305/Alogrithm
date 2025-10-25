def BMI(w,h):
    b = 10000 * w // (h**2)
    return b

h,w = map(int,input().split())

b = BMI(w,h)

print(b)
if b>25:
    print("Obesity")