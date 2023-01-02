def solution(n):
    answer = 0
    num = bin(n)[2:]
    one = num.count('1')
    while True :
        n += 1
        num = bin(n)[2:]
        two = num.count('1')
        if one == two :
            return n
