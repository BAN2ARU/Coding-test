def solution(arr):
    answer = []
    tmp = 10
    for i in (arr) :
        if i == tmp :
            continue
        answer.append(i)
        tmp = i
    return answer