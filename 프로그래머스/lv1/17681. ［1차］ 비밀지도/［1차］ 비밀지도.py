def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2) :
        ans = ''
        a = bin(a)[2:]
        b = bin(b)[2:]
        tmp = int(a)+int(b)
        for i in map(int, str(tmp)) :
            if i > 0 :
                ans += '#'
            else :
                ans += ' '
        answer.append(' '*(n-len(ans))+ans)
    return answer