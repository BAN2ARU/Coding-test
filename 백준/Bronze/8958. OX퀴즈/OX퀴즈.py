import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    test = input()
    ans, cnt = 0, 0
    for t in test :
        if t == 'O' :
            ans += 1+cnt
            cnt += 1
        else :
            cnt = 0
    print(ans)
