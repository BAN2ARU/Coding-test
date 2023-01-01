def solution(s):
    answer = 0
    slist = s.split()
    
    for i, x in enumerate(slist) :
        if x != 'Z' :
            answer += int(slist[i])
        else :
            answer -= int(slist[i-1])
    return answer