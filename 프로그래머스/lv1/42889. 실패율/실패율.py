def solution(N, stages):
    answer = []
    l = len(stages)
    for i in range(1, N+1) :
        num = stages.count(i)
        if l != 0 :
            answer.append(num/l)
        elif l == 0 :
            answer.append(0)
        l -= num
    
    array = [i for i in range(1, N+1)]
    array.sort(key = lambda x : (-answer[x-1], x))
    
    return array