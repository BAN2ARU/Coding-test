def solution(n):
    answer = ''
    while True :
        if n // 3 == 0:
            answer += str(n%3)
            break
        answer += str(n%3)
        n = n // 3
    n = str(int(answer))[::-1]
    answer = 0
    cnt = 1
    for i in str(n) :
        answer += int(i)*cnt
        cnt *= 3
    return answer