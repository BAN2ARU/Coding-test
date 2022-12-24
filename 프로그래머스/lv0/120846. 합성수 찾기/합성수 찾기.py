def solution(n):
    answer = 0
    
    for i in range(3, n+1) :
        if int(i**0.5) == i**0.5 :
            answer += 1
        else :
            cnt = 0
            for j in range(2, i//2) :
                if i % j == 0 :
                    cnt += 1
                    break
            if cnt > 0 :
                answer+=1
    return answer