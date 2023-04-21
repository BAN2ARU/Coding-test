n = int(input())

for _ in range(n) :
    sample = input().split()
    answer = list()
    for s in sample :
        answer.append(s[::-1])
    print(' '.join(answer))