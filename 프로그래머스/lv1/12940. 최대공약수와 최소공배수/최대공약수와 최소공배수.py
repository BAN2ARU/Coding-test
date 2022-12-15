def solution(n, m):
    answer = []
    for a in range(min(n,m),0,-1) :
        if n % a == 0 and m%a == 0:
            answer.append(a)
            break
    for b in range(max(n,m), n*m+1) :
        if b % n == 0 and b % m == 0 :
            answer.append(b)
            break
    return answer