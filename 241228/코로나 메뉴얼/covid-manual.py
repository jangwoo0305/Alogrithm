# 입력값 저장
people = []  # 각 사람의 (symptom, temperature)를 저장할 리스트

# 3명 입력받기
for _ in range(3):
    symptom, temperature = input().split()
    temperature = int(temperature)
    people.append((symptom, temperature))  # 튜플 형태로 저장

# 위급 상황 판단
emergency_count = 0

for symptom, temperature in people:
    if symptom == "Y" and temperature >= 37:
        emergency_count += 1

if emergency_count >= 2:
    print("E")  # 위급상황
else:
    print("N")  # 정상
