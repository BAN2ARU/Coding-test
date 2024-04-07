def solution(num_list):
    for i, num in enumerate(num_list) :
        if int(num) < 0 :
            return i
    return -1