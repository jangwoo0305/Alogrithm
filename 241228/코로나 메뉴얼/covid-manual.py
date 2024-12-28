results = []

for _ in range(3):
    symptom, temperature = input().split()
    temperature = int(temperature)
    
    if symptom == 'Y' and temperature >= 37:
        results.append('A')
    elif symptom == 'N' and temperature >= 37:
        results.append('B')
    elif symptom == 'Y' and temperature < 37:
        results.append('C')
    else:  # symptom == 'N' and temperature < 37
        results.append('D')

if results.count('A') >= 2:
    print("E")  
else:
    print("N")  
