def solution(food):
    answer = '0'
    a = food[::-1]
    for i, num in enumerate(a[:-1]) :
        tmp = (str(len(food) - i-1) * (num // 2))
        answer = tmp + answer + tmp 
    return answer