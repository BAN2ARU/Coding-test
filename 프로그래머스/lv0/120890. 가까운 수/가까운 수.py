def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x))
    answer = array[0]
    return answer