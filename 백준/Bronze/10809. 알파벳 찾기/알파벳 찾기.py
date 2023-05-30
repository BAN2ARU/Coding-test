import sys
input = sys.stdin.readline

alpha='abcdefghijklmnopqrstuvwxyz'
word = input().rstrip()

for s in alpha :
    print(word.find(s), end=' ')