def solution(board):
    answer = set()
    for i, n in enumerate(board) :
        for j, m in enumerate(board[i]) :
            if m :
                answer.update([(i+a, j+b) for a in [-1,0,1] for b in [-1, 0, 1]])
    l = len(board)

    return l*l - len([(i,j) for (i, j) in answer if(0<=i<l and 0<=j<l) ])