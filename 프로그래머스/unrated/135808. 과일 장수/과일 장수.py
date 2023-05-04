def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0
    for i in range(m, len(score)+1, m) :
        answer += min(score[i-m:i]) * m
    
    return answer