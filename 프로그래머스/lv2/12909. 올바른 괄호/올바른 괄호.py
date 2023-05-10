def solution(s):
    answer = True
    tmp = list()
    
    for i in s :
        if not tmp :
            tmp.append(i)
        elif tmp[-1]+i == '()':
            tmp.pop()
        else :
            tmp.append(i)        

    return False if tmp else True