def solution(progresses, speeds):
    answer = []
    
    for p, s in zip(progresses, speeds) :
        answer.append((100 - p - 1) // s + 1)
    
    dday = answer[0]
    cnt = 0
    re = []
    
    for i, a in enumerate(answer[1:], start=1) :
        if max(dday, a) != dday :
            dday = a
            re.append(i-cnt)
            cnt = i
        if i == len(answer)-1 :
            re.append(len(answer) - cnt)
    return re