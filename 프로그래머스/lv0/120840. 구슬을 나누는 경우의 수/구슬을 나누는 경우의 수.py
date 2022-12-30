def mult(a, b) :
    tmp = 1
    for i in range(a, b+1) :
        tmp *= i
    return tmp

def solution(balls, share):
    answer_1 = mult(share+1,balls)
    answer_2 = mult(1, balls-share)
    return answer_1//answer_2