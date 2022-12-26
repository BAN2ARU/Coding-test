def solution(n):
    cnt = 0
    for i in range(n) :
        cnt += 1
        while(cnt % 3 == 0 or '3' in str(cnt)) :
            cnt += 1
            
    return cnt