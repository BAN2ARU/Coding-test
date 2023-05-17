import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    num, word = input().split()
    for s in word :
        print(s*int(num), end='')
    print()