def solution(score):
    score = [sum(s) for s in score]
    s_score = sorted(score, reverse=True)
    return [s_score.index(i)+1 for i in score]