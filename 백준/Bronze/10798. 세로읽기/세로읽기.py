import sys
input = sys.stdin.readline

str_list = [list(input().rstrip()) for _ in range(5)]

answer = ''

for i in range(15) :
    for j in range(5) :
        try :
            answer += str_list[j][i]
        except :
            pass

print(answer)