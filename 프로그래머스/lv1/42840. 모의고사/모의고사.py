def solution(answers):
    answer = []
    l = len(answers)
    one = [1, 2, 3, 4, 5] * ((l // 5) + 1)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * ((l // 8) + 1)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((l // 10) + 1)
    a1, b2, c3 = 0, 0, 0
    for i, num in enumerate(answers) :
        if num == one[i] :
            a1 += 1
        if num == two[i] :
            b2 += 1
        if num == three[i] :
            c3 += 1
    ans = sorted([a1, b2, c3], reverse=True)
    
    if ans.index(a1) == 0 :
        answer.append(1)
    if ans.index(b2) == 0 :
        answer.append(2)
    if ans.index(c3) == 0 :
        answer.append(3)
    
    return answer
    
    
    