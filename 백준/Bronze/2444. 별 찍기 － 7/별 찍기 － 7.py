import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, 2*n) :
    tmp = abs(n-i)
    if i<= n :
        star = 2*i -1
    else :
        star = (2*n-i)*2 -1
    print(' '*tmp+'*'*star)
