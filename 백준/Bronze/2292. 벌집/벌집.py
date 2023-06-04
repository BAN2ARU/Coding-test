import sys
input = sys.stdin.readline

n = int(input())

cnt, num = 1, 1

while(n > num) :
    cnt += 1
    num += 6*(cnt-1)

print(cnt)
