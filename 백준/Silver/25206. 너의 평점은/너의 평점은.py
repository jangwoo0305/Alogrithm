# 전공평점 = 전공과목별(학점 * 과목평점)의 합을 학점의 총합으로 나눈 값
def Graduation():
    avg = {'A+':4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
    major_subsum = 0
    total_value = 0
    for _ in range(20):
        N = input().split() # 과목명, 학점, 등급
        value = float(N[1])
        if N[2] != 'P':
            total_value += value
        grade = str(N[2])

        for k,v in avg.items():
            if grade == k:
               major_subsum += value * v
    print(major_subsum/total_value)

if __name__ == "__main__":
    Graduation()



