def solution(a, b, c):
    result = a + b + c;
    
    if(a == b or a == c or b == c):
        result *= a ** 2 + b ** 2 + c ** 2;
        
    if a == b == c:
        result *= a ** 3 + b ** 3 + c ** 3;
        
    return result;