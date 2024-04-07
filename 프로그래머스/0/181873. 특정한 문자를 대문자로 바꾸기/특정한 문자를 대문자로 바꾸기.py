def solution(my_string, alp):
    return ''.join(list(mystr.upper() if mystr== alp else mystr for mystr in my_string))