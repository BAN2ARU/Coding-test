def solution(arr):
    answer = [arr[0]]
    for a in arr[1:] :
        if answer[-1] == a :
            continue
        answer.append(a)
    
    return answer