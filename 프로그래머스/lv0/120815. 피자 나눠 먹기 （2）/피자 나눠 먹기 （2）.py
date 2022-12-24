def solution(n):
    a = max(6, n)
    b = min(6, n)
    val = lambda a,b : b if a%b == 0 else val(b, a%b) 
    return n // val(a,b)