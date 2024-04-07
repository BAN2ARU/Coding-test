def solution(a, b):
    num1 = int(str(a)+str(b))
    num2 = 2*a*b
    return num2 if num1 < num2 else num1