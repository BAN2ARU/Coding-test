def solution(spell, dic):
    answer = 0
    for d in dic :
        for i in range(len(spell)) :
            if d.count(spell[i]) != 1:
                break
            elif i == len(spell)-1 and d.count(spell[i]) == 1:
                return 1
    return 2