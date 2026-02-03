number = []
for i in range(9):
    number.append(int(input()))
    
max_val = 0
max_ind = 0

for i,digit in enumerate(number):
    if digit > max_val:
        max_val = digit
        max_ind = i + 1
        
print(max_val)
print(max_ind)
    