import sys
input = sys.stdin.readline

word = input().rstrip().upper()
uniq = list(set(word))

cnt = list()
for s in uniq :
    cnt.append(word.count(s))

maximum = max(cnt)
if cnt.count(maximum) > 1 :
    print('?')
else :
    print(uniq[cnt.index(maximum)])