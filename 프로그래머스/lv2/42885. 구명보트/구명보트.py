def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    b = len(people)-1
    for a in range(b+1) :
        if a == b :
            answer += 1
            break
        elif a > b :
            break
        else :
            if people[a] + people[b] <= limit :
                answer += 1
                b -= 1
            else :
                answer += 1
        
    return answer