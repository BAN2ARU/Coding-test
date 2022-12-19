def solution(n, m):
    a = max(n,m)
    b = min(n, m)
    max_value = lambda a,b : b if not a%b else max_value(b, a%b)
    m = max_value(a, b)
    return [m, a*b//m]