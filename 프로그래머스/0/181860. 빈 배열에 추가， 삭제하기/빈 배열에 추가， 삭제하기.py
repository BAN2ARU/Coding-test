def solution(arr, flag):
    answer = ''
    for i, fl in enumerate(flag) :
        if fl :
            answer += str(arr[i]) * arr[i] * 2
        else :
            answer = answer[:-arr[i]]
    return list(map(int, ''.join(answer)))