def solution(my_str, n):
    answer = []
    a = 0
    while True :
        a += n
        if a >= len(my_str) :
            answer.append(my_str[a-n:])
            break
        answer.append(my_str[a-n:a])
    return answer