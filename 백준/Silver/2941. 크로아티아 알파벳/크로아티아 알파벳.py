import sys
input = sys.stdin.readline

word = input().rstrip()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i, s in enumerate(cro) :
    word = word.replace(s, str(i))

print(len(word))