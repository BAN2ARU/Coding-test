def solution(score):
    score = [sum(s) for s in score]
    score_sum = sorted(score, reverse=True)
    return [score_sum.index(s)+1 for s in score]