def solution(s):
    tmp = list(s[0])
    for i in s[1:] :
        if not tmp :
            tmp.append(i)
        elif tmp[-1] + i == '()' :
            tmp.pop()
        else :
            tmp.append(i)
    return False if len(tmp) else True