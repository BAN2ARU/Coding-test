def solution(brown, yellow):
    answer = []
    color = brown + yellow
    for i in range(3, color+1) :
        if (color) % i == 0 :
            if (brown - 2*i + 4)/2 == yellow/(i-2) + 2 :
                return [yellow/(i-2) + 2,i]