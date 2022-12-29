def solution(s):
    cnt = 0
    zero = 0

    while(True) :
        if s=='1' :
            return[cnt, zero]
        zero += s.count('0')
        s = len(s.replace('0', ''))
        tmp = ''
        while (s>1) :
            tmp += str(s%2)
            s = s//2
        s = '1' + tmp[::-1]
        cnt += 1
        