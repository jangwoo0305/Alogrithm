C = int(input())

for i in range(C):
    scores = list(map(int,input().split()))
    avg = sum(scores[1:])/scores[0]
    
    avghigh_student = 0 #평균 점수 이상인 학생 수
    
    for j in scores[1:]:
        if j > avg:
            avghigh_student += 1
    
    rateavghigh_student = avghigh_student/scores[0]*100
    print(f"{rateavghigh_student:.3f}%")