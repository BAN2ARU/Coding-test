def solution(my_string, letter):
    my_string = list(map(str, my_string))
    while letter in my_string :
        my_string.remove(letter)
    return ''.join(my_string)