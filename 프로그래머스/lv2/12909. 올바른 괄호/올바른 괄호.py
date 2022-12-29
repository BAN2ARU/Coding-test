def solution(s):
    a = []
    b = []
    
    for i, value in enumerate(s) :
        if value == '(' :
            a.append(i)
        else :
            b.append(i)    
    if len(a) != len(b) :
        return False
    for a_value, b_value in zip(a,b) :
        if b_value < a_value :
            return False
    return True