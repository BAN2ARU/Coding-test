def solution(board):
    bomb = set()
    for i, n in enumerate(board) :
        for j, m in enumerate(board[i]) :
            if m :
                bomb.update((i+a,j+b) for a in [-1, 0, 1] for b in [-1, 0, 1])
    l = len(board)
    return l*l - sum(0<=i<l and 0<=j<l for i,j in bomb)