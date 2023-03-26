def solution(n):
    answer = 0
    for i in range(1, n+1) :
        while True :
            answer += 1
            if (answer%3 == 0) or ('3' in str(answer)) :
                continue
            else :
                break
    return answer