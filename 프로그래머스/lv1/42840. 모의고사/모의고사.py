def solution(answers):
    one = '12345'
    two = '21232425'
    thr = '3311224455'
    l_one = len(one)
    l_two = len(two)
    l_thr = len(thr)
    answer = [0, 0, 0]
    
    for i, ans in enumerate(answers) :
        if ans == int(one[i%l_one]) :
            answer[0] += 1
        if ans == int(two[i%l_two]) :
            answer[1] += 1
        if ans == int(thr[i%l_thr]) :
            answer[2] += 1
    
    correct = list()
    max_n = max(answer)
    
    for i, n in enumerate(answer) :
        if max_n == n :
            correct.append(i+1)
    
    return correct