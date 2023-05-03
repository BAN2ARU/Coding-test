import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

print(nlist.count(int(input())))