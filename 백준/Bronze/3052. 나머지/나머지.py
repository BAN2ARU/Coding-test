import sys

input = sys.stdin.readline

ans = set()

for _ in range(10) :
    num = int(input())
    ans.add(num % 42)

print(len(ans))
