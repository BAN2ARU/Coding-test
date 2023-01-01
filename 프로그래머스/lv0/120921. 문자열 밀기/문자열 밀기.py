def solution(A, B):
    answer = 0
    for i in range(len(A)) :
        tmp = A[-i:] + A[:-i]
        if tmp == B :
            return i
    return -1