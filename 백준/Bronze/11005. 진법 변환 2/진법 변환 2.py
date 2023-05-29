import sys
input = sys.stdin.readline

N, B = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''

while True :
    answer += str(num[N%B])
    N = N // B
    if N == 0 :
        break

print(answer[::-1])