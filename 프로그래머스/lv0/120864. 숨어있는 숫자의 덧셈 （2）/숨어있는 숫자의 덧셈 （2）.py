def solution(my_string):
    return sum(map(int, (''.join(s if s.isdigit() else ' ' for s in my_string)).split()))