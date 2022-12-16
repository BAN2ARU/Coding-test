def solution(s):
    answer = ''
    cnt = 0
    for i in s :
        cnt += 1
        if i == ' ' :
            cnt = 0
            answer += i
            continue
        if cnt % 2 == 1 :
            answer += i.upper()
        else :
            answer += i.lower()

    return answer