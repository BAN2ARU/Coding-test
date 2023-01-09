import math
def solution(clothes):
    answer = 1
    c_dict = dict()
    for c in clothes :
        try :
            c_dict[c[1]] += 1
        except :
            c_dict[c[1]] = 2
    for c in list(c_dict.values()) :
        answer *= c
        
    return answer - 1