def solution(score):
    score = [sum(i) for i in score]
    rank = sorted(score, reverse=True)
    return [rank.index(i)+1 for i in score]