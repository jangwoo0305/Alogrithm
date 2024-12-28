people = []

for _ in range(3):
    symptom, temperature = input().split()
    temperature = int(temperature)
    people.append((symptom, temperature))

emergency_count = 0

for symptom, temperature in people:
    if symptom == "Y" and temperature >= 37:
        emergency_count += 1

if emergency_count => 2:
    print("E")
else:
    print("N")

