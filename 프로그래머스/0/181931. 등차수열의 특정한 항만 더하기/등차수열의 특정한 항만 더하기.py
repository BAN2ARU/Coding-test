def solution(a, d, included):
    answer, num = 0, 0
    for i in range(len(included)) :
        if included[i] :
            answer += a
            num += i
    return answer + d*num