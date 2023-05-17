import sys
input = sys.stdin.readline
word = input().rstrip().lower()

word_dict = dict()

for w in word :
    try :
        word_dict[w] += 1
    except :
        word_dict[w] = 1

max_n = max(word_dict.values())
cnt = 0
answer = ''

for s, n in word_dict.items() :
    if n == max_n :
        cnt+=1
        answer=s

print(answer.upper() if cnt==1 else '?')