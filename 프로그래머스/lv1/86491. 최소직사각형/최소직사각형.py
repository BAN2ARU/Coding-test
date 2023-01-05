def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for s in sizes :
        sw = min(s)
        sh = max(s)
        w = max(w, sw)
        h = max(h, sh)
    return w*h