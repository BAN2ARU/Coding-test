def solution(people, limit):
    people.sort(reverse=True)
    l = len(people) - 1
    for i in range(l+1) :
        if i >= l :
            break
        elif people[i] + people[l] <= limit :
            l -= 1
    return l+1