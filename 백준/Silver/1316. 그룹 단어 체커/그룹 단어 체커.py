import sys
input = sys.stdin.readline

cnt = 0
num = int(input())

for _ in range(num) :
    word = input().rstrip()
    tmp = ''
    for w in word :
        if not tmp :
            tmp += w
        elif w == tmp[-1] :
            pass
        elif w in tmp :
            cnt += 1
            break
        else :
            tmp += w
       
print(num-cnt)