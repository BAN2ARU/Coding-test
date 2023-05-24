def solution(s):
    answer = []
    zero, cnt = 0, 0
    while (s!='1') :
        cnt += 1
        one = s.count('1')
        zero += len(s) - one
        
        s = bin(one)[2:]
    return [cnt, zero]