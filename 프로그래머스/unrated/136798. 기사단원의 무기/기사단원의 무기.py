def solution(number, limit, power):
    answer = 1
    for num in range(2, number+1) :
        cnt = 0
        for n in range(1, int(num**0.5)+1) :
            if num % n == 0 :
                if n == num**0.5 :
                    cnt += 1
                else :
                    cnt += 2
            if cnt > limit :
                break
        if cnt > limit :
            answer += power
            continue
        answer += cnt
    return answer