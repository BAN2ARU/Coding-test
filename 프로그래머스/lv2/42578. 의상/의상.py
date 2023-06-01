def solution(clothes):
    clo_dict = dict()
    
    for a, b in clothes :
        try :
            clo_dict[b] += 1
        except :
            clo_dict[b] = 2
    
    answer = 1
    
    for i in clo_dict.values() :
        answer *= i 
    
    return answer-1