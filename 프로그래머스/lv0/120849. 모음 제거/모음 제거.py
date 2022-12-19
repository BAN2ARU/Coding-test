def solution(my_string):
    answer = ''
    for my_str in my_string :
        if my_str in ['a', 'e', 'i', 'o', 'u'] :
            continue
        answer += my_str
    return answer