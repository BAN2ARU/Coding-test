def solution(price):
    discount = {500000:0.8, 300000:0.9, 100000:0.95}
    
    for dis_price, dis_rate in discount.items() :
        if price >= dis_price :
            return int(price*dis_rate)
    return price