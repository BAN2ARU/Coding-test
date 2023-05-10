def solution(a, b):
    eq = lambda x,y : y if x%y==0 else eq(y, x%y)
    num = b // eq(a,b)
    while True :
        if num % 2 == 0 :
            num = num//2
        elif num % 5 == 0 :
            num = num//5
        else :
            break
    return 1 if num==1 else 2