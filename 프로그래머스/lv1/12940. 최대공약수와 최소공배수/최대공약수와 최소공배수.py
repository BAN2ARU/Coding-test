def solution(n, m):
    eq = lambda x, y : y if x % y == 0 else eq(y, x%y)
    num = eq(n,m)
    return [num, n*m//num]