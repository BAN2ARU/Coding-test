def solution(score):
    answer = []
    temp = []
    score = [sum(s)/2 for s in score]
    scores = sorted(score,reverse=True)
    ans_dict = dict()
    tmp = 0
    tmp_score = 0
    for s in scores :
        if temp[-1:] != [s] :
            tmp += 1 + tmp_score
            temp.append(s)
            ans_dict[s] = tmp
            tmp_score = 0
        else :
            tmp_score += 1
            
    for s in score :
        answer.append(ans_dict[s])
    return answer