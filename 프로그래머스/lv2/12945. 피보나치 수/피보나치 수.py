def solution(n):
    nlist = [0] * int(n+1)
    nlist[1] = 1
    for i in range(2, n+1) :
        nlist[i] = int(nlist[i-1]) + int(nlist[i-2])
    return nlist[n] % 1234567