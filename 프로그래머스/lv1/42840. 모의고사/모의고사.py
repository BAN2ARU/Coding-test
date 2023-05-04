def solution(answers):
    l = len(answers)
    one = [1,2,3,4,5] * (l//5+1) 
    two = [2,1,2,3,2,4,2,5] * (l//8+1) 
    thr = [3,3,1,1,2,2,4,4,5,5] * (l//10+1)
    score = [0,0,0]
    for an, on, tw, th in zip(answers, one, two, thr) :
        if an == on :
            score[0] += 1
        if an == tw :
            score[1] += 1
        if an == th :
            score[2] += 1
    m = max(score)
    num = [1, 2, 3]
    answer = list()
    
    for i in range(len(score)):
        if score[i] == m :
            answer.append(num[i])
    return answer