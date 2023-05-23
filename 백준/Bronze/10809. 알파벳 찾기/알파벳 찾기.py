import sys
input = sys.stdin.readline

alpha = 'abcdefghijklmnopqrstuvwxyz'
word = input().rstrip()
answer = [-1] * len(alpha)

for i, s in enumerate(alpha) :
    if s in word :
        answer[i] = word.index(s)
        
print(*answer)