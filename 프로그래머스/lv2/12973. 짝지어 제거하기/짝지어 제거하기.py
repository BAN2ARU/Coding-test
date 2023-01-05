def solution(s):
    tmp = []
    
    for word in s :
        if tmp[-1:] == [word] :
            tmp.pop()
        else :
            tmp.append(word)

    return 0 if tmp else 1