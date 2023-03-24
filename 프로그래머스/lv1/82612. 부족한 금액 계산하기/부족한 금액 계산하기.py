def solution(price, money, count):
    price = price*sum(range(1, count+1)) - money
    return price if price>0 else 0