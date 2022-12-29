def solution(s):
    answer = s[0].upper()
    for i in s[1:] :
        if answer[-1:] == ' ' :
            answer += i.upper()
        else :
            answer += i.lower()
    return answer