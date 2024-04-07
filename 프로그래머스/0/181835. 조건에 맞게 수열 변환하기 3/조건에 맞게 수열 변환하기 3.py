def solution(arr, k):
    return list(k*num for num in arr) if k%2==1 else list(k+num for num in arr)