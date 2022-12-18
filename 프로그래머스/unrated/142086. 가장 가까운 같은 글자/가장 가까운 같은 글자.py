def solution(slist):
    tmp = []
    answer = []
    for s in slist :
        if s in tmp :
            answer.append(tmp[::-1].index(s) + 1)
            tmp.append(s)
        else :
            answer.append(-1)
            tmp.append(s)
    return answer