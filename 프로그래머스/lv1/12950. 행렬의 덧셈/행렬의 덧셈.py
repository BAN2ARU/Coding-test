def solution(arr1, arr2):
    answer = [[a+b for a,b in zip(a1, b1)] for a1, b1 in zip(arr1, arr2)]
    return answer