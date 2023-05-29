def solution(my_string):
    answer = 0
    my_str = ''.join(s if s.isdigit() else ' ' for s in my_string)
    return sum(map(int, my_str.split()))