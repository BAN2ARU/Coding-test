import sys

input = sys.stdin.readline

student = {i for i in range(1, 31)}
tmp = set()

for _ in range(28) :
    tmp.add(int(input()))

lst = sorted(list(student-tmp))


for i in range(2):
    print(lst[i])