def solution(answers):
    answer = [0, 0, 0]
    l = len(answers)
    one = [1, 2, 3, 4, 5] * ((l-1)//5 + 1)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * ((l-1)//8 + 1)
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((l-1)//10 + 1)

    for a, b, c, ans in zip(one, two, thr, answers) :
        if a == ans :
            answer[0] += 1
        if b == ans :
            answer[1] += 1
        if c == ans :
            answer[2] += 1
    
    winner = list()
    max_n = max(answer)
    for i, n in enumerate(answer) :
        if n == max_n :
            winner.append(i+1)
    return winner