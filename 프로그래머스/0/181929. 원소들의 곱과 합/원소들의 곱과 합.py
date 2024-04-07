def solution(num_list):
    ans = 1
    for num in num_list :
        ans *= num
    if ans < sum(num_list)**2 :
        return 1
    return 0