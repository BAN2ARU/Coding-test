def solution(score):
    score = [sum(s) for s in score]
    rank = sorted(score, reverse=True)
    return [rank.index(s)+1 for s in score]