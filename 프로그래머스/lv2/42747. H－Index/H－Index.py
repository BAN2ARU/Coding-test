def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(citations[0], -1, -1) :
        tmp = 0
        for c in citations :
            if c >= i :
                tmp += 1
                if tmp == i :
                    return(i)
            else :
                break
    return 0