def solution(price, money, count):    
    tmp = price * (count+1) * 0.5 *count - money
    return tmp if tmp >= 0 else 0
    