def solution(n):
    answer = []
    for i in range(2, n//2+1) :
        if n%i == 0 :
            cnt = 0
            for a in answer :
                if i % a == 0 :
                    cnt += 1
                    break
            if cnt == 0 :
                answer.append(i)
    cnt = 0
    for a in answer :
        if n % a == 0 :
            cnt += 1
            break
    if cnt == 0 :
        answer.append(n)
    return answer