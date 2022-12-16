def solution(price, money, count):
    answer = (price * count + price) / 2 * count
    if answer - money > 0 :
        return answer-money
    return 0
