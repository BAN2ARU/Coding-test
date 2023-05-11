def solution(clothes):
    answer = 1
    clo_dict = dict()
    
    for a, b in clothes :
        try :
            clo_dict[b] += 1
        except :
            clo_dict[b] = 1
            
    for a, b in clo_dict.items() :
        answer = answer * (b+1)
    return answer -1