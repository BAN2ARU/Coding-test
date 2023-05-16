def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    l = len(people)
    b = l-1
    for a in range(l) :
        if a >= b :
            break
        else :
            if people[a] + people[b] <= limit :
                b -= 1
                answer += 1
    return l-answer