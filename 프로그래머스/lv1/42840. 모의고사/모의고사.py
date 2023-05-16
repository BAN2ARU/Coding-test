def solution(answers):
    answer = [0, 0, 0]
    ans = list()
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    l1 = len(one)
    l2 = len(two)
    l3 = len(thr)
    
    for i, n in enumerate(answers) :
        if one[i%l1] == n :
            answer[0] += 1
        if two[i%l2] == n :
            answer[1] += 1
        if thr[i%l3] == n :
            answer[2] += 1
            
    num = max(answer)
    
    for i, n in enumerate(answer) :
        if n == num :
            ans.append(i+1)
    return ans