def solution(board, k):
    answer = 0
    i, j = len(board), len(board[0])
    for a in range(i) :
        for b in range(j) :
            if a+b <= k :
                answer += board[a][b]
    
    return answer