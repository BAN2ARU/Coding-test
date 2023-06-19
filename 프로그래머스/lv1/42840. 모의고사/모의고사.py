def solution(answers):
    answer = [0, 0, 0]
    one = '12345'
    two = '21232425'
    thr = '3311224455'
    len_1 = len(one)
    len_2 = len(two)
    len_3 = len(thr)
    
    for i, ans in enumerate(answers) :
        if int(one[i%len_1]) == ans :
            answer[0] += 1
        if int(two[i%len_2]) == ans :
            answer[1] += 1
        if int(thr[i%len_3]) == ans :
            answer[2] += 1
    
    max_n = max(answer)
    ans = list()
    
    for i, n in enumerate(answer) :
        if n == max_n :
            ans.append(i+1)
    
    return ans