t = int(input())
for _ in range(t) :
    answer = 0
    tlist = list(map(int, input().split()))
    n = int(input())
    for j in range(n) :
        nlist = list(map(int, input().split()))
        tmp0 = ((tlist[0]-nlist[0])**2 + (tlist[1]-nlist[1])**2)**0.5
        tmp1 = ((tlist[2]-nlist[0])**2 + (tlist[3]-nlist[1])**2)**0.5
        if (tmp0 < nlist[2] and tmp1>=nlist[2]) or (tmp1<nlist[2] and tmp0 >= nlist[2]) :
            answer += 1
    print(answer)