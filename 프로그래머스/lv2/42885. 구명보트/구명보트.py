def solution(people, limit):
    people.sort(reverse=True)
    j = len(people) - 1
    
    for i in range(len(people)) :
        if i >= j :
            break
        if people[i] + people[j] <= limit :
            j -= 1
    
    return j+1