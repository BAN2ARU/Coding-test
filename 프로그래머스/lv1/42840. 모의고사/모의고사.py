def solution(answers):
    one = [1,2,3,4,5]    
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    
    l1, l2, l3 = len(one), len(two), len(thr)
    rank = [0, 0, 0]
    
    for i, ans in enumerate(answers) :
        if ans == one[i%l1] :
            rank[0] += 1
        if ans == two[i%l2] :
            rank[1] += 1
        if ans == thr[i%l3] :
            rank[2] += 1

    answer = list()
    first = max(rank)
    
    for i, n in enumerate(rank) :
        if n == first :
            answer.append(i+1)
    
    return answer