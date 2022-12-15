def solution(price, money, count):
    a = price*sum(range(1, count+1)) - money
    if a > 0 :
        return a
    else :
        return 0 