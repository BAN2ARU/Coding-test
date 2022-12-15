def solution(arr):
    answer = [arr[0]]
    for i in (arr[1:]) :
        if answer[-1] == i :
            continue
        answer.append(i)
    return answer