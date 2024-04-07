def solution(todo_list, finished):
    answer = []
    for a,b in zip(todo_list, finished) :
        if not b :
            answer.append(a)
    return answer