import sys

input = sys.stdin.readline

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = [-1] * len(alpha)
word = input()

for i, s in enumerate(alpha) :
    if s in word :
        answer[i] = word.index(s)

print(*answer)        
