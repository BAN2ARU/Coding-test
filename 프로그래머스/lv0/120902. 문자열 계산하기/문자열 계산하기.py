def solution(my_string):
    my_string = my_string.replace(' - ', ' + -')
    my_string = my_string.split('+')
    return sum([int(i) for i in my_string])