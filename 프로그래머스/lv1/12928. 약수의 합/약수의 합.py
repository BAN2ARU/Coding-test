def solution(n):
    answer = 0
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    for i in range(1, n//2+1) :
        if n % i == 0 :
            answer += i
    return answer+n