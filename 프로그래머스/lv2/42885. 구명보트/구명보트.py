def solution(people, limit):
    people.sort(reverse=True)
    l = len(people)
    b = l-1
    a = 0
    for i in range(l) :
        if i >=b :
            break
        elif people[i]+people[b] <= limit :
            b -= 1
            a += 1
    
    return l-a