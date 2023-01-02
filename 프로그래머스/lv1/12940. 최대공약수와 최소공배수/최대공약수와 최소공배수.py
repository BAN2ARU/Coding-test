def solution(n, m):
    a = min(n, m)
    b = max(n, m)
    eq1 = lambda a,b : b if a%b == 0 else eq1(b, a%b)
    v1 = eq1(b, a)
    return [v1, a*b//v1]