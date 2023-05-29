def solution(board):
    l = len(board)
    bomb = set()
    for i, n in enumerate(board) :
        for j, m in enumerate(board[i]) :
            if m :
                bomb.update((i+a, j+b) for a in [-1, 0, 1] for b in [-1, 0, 1])
            
    return l**2 - sum(0<=i<l and 0<=j<l for i,j in bomb )