def solution(bin1, bin2):
    answer = int(bin1,2) + int(bin2,2)
    result = ''
    
    while True :
        result += str(answer%2)
        answer = answer // 2
        if answer == 0 :
            break

    return ''.join(result[::-1])