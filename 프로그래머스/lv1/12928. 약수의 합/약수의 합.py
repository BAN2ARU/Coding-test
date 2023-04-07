def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1) :
        if n % i == 0 :
            if i == n**0.5 :
                answer += i
                continue
            answer += (i + n//i)
            
    return answer