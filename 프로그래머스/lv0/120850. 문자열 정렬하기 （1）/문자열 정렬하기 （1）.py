def solution(my_string):
    answer = []
    for s in my_string :
        try :
            s = int(s)
            answer.append(s)
        except :
            pass
    return sorted(answer)