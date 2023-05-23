def solution(a, b, n):
    answer = 0
    while True :
        back = n//a * b
        answer += back
        n = back + n%a
        if n<a :
            break
    return answer