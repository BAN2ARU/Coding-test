import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    ps = input().rstrip()

    tmp = list(ps[0])

    for s in ps[1:] :
        if not tmp :
            tmp.append(s)
        elif tmp[-1]+s == '()' :
            tmp.pop()
        else :
            tmp.append(s)

    print("NO") if tmp else print("YES")