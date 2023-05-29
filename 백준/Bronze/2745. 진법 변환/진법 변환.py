import sys
input = sys.stdin.readline

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = input().rstrip().split()
B = int(B)
answer = 0
l = len(N)-1

for i in N :
    answer += int(num.index(i)*(B**l))
    l -= 1

print(answer)
