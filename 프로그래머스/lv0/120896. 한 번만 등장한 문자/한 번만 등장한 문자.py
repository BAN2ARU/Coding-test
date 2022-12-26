def solution(s) :
    answer = ''
    sset = sorted(set(s))
    
    for ss in sset :
        if s.count(ss) == 1 :
            answer += ss
    
    return answer