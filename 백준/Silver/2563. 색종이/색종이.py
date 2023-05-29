import sys
input = sys.stdin.readline

n = int(input())
answer = set()

for _ in range(n) :
    a, b = map(int, input().split())
    answer.update((i, j) for i in range(a,a+10) for j in range(b, b+10))

print(len(answer))