def solution(array, n):
    array.sort(reverse=True)
    answer = 0
    thr = 100
    for a in array :
        tmp = a-n
        if abs(tmp) <= thr :
            thr = abs(tmp)
            answer = a
    return answer
    