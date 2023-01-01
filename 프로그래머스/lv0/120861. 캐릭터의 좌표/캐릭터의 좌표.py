def solution(keyinput, board):
    max_x = board[0] // 2
    max_y = board[1] // 2
    min_x = -1 * max_x
    min_y = -1 * max_y
    x,y = 0,0
    for key in keyinput :
        if key == 'left' :
            x -= 1
            x = max(min(x, max_x), min_x)
        elif key  == 'right' :
            x += 1
            x = max(min(x, max_x), min_x)
        elif key == 'up' :
            y+= 1
            y = max(min(y, max_y), min_y)
        else :
            y-= 1
            y = max(min(y, max_y), min_y)
    return [x,y]