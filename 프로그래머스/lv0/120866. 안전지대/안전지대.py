def solution(board):
    danger = set()
    l = len(board)
    for i,n in enumerate(board) :
        for j,m in enumerate(board[i]) :
            if m :
                danger.update((i+a,j+b) for a in [-1,0,1] for b in [-1,0,1])
    return l*l - sum(0<=a<l and 0<=b<l for a,b in danger)