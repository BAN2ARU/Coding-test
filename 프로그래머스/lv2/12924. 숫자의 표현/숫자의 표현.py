def solution(n):
    answer = 0
    for i in range(2, n+1) :
        if i % 2 == 0 :
            if n % i == i/2 and (n//i - n%i + 1) > 0 :
                answer += 1
        else :
            if n % i == 0 and (n//i - i//2) > 0:
                answer += 1
    return answer+1