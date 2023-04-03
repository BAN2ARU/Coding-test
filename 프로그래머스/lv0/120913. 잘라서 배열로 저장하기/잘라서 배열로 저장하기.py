def solution(my_str, n):
    return [my_str[i*n:(i+1)*n] for i in range((len(my_str)-1)//n+1)]