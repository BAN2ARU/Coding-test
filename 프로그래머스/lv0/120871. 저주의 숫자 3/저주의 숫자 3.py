def solution(n):
    cnt = 0
    val = 0
    while True :
        cnt += 1
        val += 1
        while True :
            if val % 3 == 0 or '3' in str(val) :
                val += 1
            else :
                break
        if cnt == n :
            return val