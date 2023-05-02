def solution(people, limit):
    people = sorted(people, reverse=True)
    j = len(people) - 1
    
    for i in range(len(people)) :
        if people[i] + people[j] <= limit :
            j -= 1
        if i >= j :
            print(i, j)
            break
        
    return i+1