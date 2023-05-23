def solution(clothes):
    clo_dicts = dict()
    
    for a,b  in clothes :
        try :
            clo_dicts[b] += 1
        except :
            clo_dicts[b] = 2
    
    answer = 1
    for i in clo_dicts.values() :
        answer = answer*i
    return answer-1