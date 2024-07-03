def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    j = -1
    for i in range(n) :
        j += 1
        answer[i][j] = 1
        
    return answer