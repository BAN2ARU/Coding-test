def solution(n):
    answer = [n]
    while True :
        if n % 2 == 0 :
            n = n // 2
        else :
            n = n*3 + 1
        answer.append(n)
        if n == 1 :
            return(answer)
        