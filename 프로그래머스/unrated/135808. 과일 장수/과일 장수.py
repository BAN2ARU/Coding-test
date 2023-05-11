def solution(k, m, score):
    answer = 0
    l = len(score)
    score.sort()
    return sum([m*score[i] for i in range(l%m, l, m)])