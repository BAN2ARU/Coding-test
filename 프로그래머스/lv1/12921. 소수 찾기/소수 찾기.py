def solution(n):
    answer = 0
    for num in range(2, n+1) :
        n = int(num**0.5)
        if n == 1 :
            answer += 1 
        for i in range(2, n + 1) :
            if num % i == 0 :
                break
            elif i == n :
                answer+=1
    return answer