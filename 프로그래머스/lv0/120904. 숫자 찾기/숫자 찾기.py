def solution(num, k):
    a = list(str(num))
    if str(k) in a :
            return a.index(str(k)) + 1
    return -1