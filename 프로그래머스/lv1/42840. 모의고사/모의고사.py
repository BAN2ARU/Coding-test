def solution(answers):
    one = '12345'
    two = '21232425'
    thr = '3311224455'
    l1, l2, l3 = len(one), len(two), len(thr)
    ans = [0, 0, 0]
    
    for i, n in enumerate(answers) :
        if n == int(one[i%l1]) :
            ans[0] += 1
        if n == int(two[i%l2]) :
            ans[1] += 1
        if n == int(thr[i%l3]) :
            ans[2] += 1
    max_n = max(ans)
    answer = list()
    
    for i, n in enumerate(ans) :
        if n == max_n :
            answer.append(i+1)
    
    return answer