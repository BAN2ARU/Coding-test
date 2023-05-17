def solution(a, b, n):
    answer = 0
    while n//a>0 :
        num = n//a * b
        answer += num
        n = num + n%a
    return answer