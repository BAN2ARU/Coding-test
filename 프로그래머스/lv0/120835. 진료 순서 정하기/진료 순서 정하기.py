def solution(emergency):
    answer = []
    copy_list = sorted(emergency, reverse=True)
    
    for e in emergency :
        answer.append(copy_list.index(e)+1)
    return answer