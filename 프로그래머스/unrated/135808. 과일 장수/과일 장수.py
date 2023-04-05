def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    
    num = len(score) // m
    
    for i in range(num) :
        answer += min(score[i*m:(i+1)*m]) *m
    return answer