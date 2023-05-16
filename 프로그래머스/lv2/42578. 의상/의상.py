def solution(clothes):
    answer = 1
    clo_dict = dict()
    for a, b in clothes :
        try :
            clo_dict[b] += 1
        except :
            clo_dict[b] = 2
    
    for i in clo_dict.values() :
        answer = answer*i
    
    return answer-1