def solution(price):
    cloth = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    for cost, rate in cloth.items() :
        if price >= cost :
            return int(price * rate)