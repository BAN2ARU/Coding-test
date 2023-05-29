import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    money = int(input())
    answer, money = divmod(money, 25)
    print(answer, end=' ')
    answer, money = divmod(money, 10)
    print(answer, end=' ')
    answer, money = divmod(money, 5)
    print(answer, end=' ')
    print(money)