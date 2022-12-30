def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    digits = my_string[2::2]
    letters = my_string[1::2]
    for a,b in zip(digits, letters) :
        print(a,b)
        if b == '+' :
            answer += int(a)
        else :
            answer -= int(a)   
    return answer