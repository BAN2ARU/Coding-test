import sys
input = sys.stdin.readline

max_num = -1
max_index = [0, 0]

for i in range(1, 10) :
    num = list(map(int, input().split()))

    if max(num) > max_num :
        max_num = max(num)
        max_index[0] = i
        max_index[1] = num.index(max_num) + 1

print(max_num)
print(*max_index)