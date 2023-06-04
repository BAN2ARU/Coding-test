import sys
input = sys.stdin.readline

n = int(input())
num_list = list()

for _ in range(n) :
    func = input()
    if 'push' in func :
        num_list.append(func.split()[1])
    elif 'pop' in func :
        if num_list :
            print(num_list[-1])
            num_list.pop()
        else :
            print(-1)
    elif 'size' in func :
        print(len(num_list))
    elif 'empty' in func :
        print(0) if num_list else print(1)
    else :
        print(num_list[-1]) if num_list else print(-1)