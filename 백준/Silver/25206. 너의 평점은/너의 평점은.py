import sys
input = sys.stdin.readline

score_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F': 0.0}

num = 0
sum_score = 0

for _ in range(20) :
    _, n, s = input().split()
    n = float(n)

    if s == 'P' :
        pass
    else :
        num += n
        sum_score += n*score_dict[s]

print(f'{sum_score/num:.6f}')

