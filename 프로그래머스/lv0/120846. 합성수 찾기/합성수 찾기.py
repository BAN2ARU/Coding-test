def solution(n):
    answer = 0
    for num in range(4, n+1) :
        for i in range(2, (num+1)//2+1) :
            if num % i == 0 :
                answer += 1
                print(num, i)
                break
    return answer