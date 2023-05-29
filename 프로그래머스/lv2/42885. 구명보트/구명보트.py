def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l = len(people)
    b = l-1
    cnt = 0
    for a in range(l) :
        if a >= b :
            break
        elif people[a] + people[b] <= limit :
            b -= 1
            cnt += 1
            
    return l - cnt