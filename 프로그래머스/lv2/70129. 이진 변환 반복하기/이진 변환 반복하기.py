def solution(s):
    cnt = 0
    zero_cnt = 0
    while (len(s) != 1) :
        cnt += 1
        tmp = s.count('1')
        zero_cnt += len(s) - tmp
        s = bin(tmp)[2:]
    return [cnt, zero_cnt]