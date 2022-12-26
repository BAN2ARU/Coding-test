def solution(price, money, count):
    answer = price*(count+1) / 2 * count
    return (answer - money) if answer > money else 0