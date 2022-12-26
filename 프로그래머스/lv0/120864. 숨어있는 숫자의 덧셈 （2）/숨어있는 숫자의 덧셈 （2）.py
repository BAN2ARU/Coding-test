def solution(my_string):
    my_string = my_string +'a'
    answer = 0
    tmp = ''
    for s in my_string :
        if s.isdigit() :
            tmp += str(s)
        else :
            if tmp : 
                answer += int(tmp)
            tmp = ''
    return answer