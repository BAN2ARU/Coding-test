def solution(answers):
    answer = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    
    len_one, len_two, len_thr = len(one), len(two), len(thr)
    
    for i, a in enumerate(answers) :
        if a == one[i%len_one] :
            answer[0] += 1
        if a == two[i%len_two] :
            answer[1] += 1
        if a == thr[i%len_thr] :
            answer[2] += 1
    
    max_num = max(answer)
    ans = list()
    
    for i, a in enumerate(answer) :
        if a == max_num :
            ans.append(i+1)
    
    return ans