import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = [0] * n
for _ in range(m) :
    a, b, c = map(int, input().split())
    for i in range(a-1, b) :
        answer[i] = c

for i in answer :
    print(i, end=' ')