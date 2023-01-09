def solution(arr):
    gcd = lambda x,y : y if x%y==0 else gcd(y,x%y)
    arr.sort(reverse=True)
    i = arr[0]
    for a in arr[1:] :
        if i % a == 0 :
            i = i
        else :
            i = i * a // gcd(i,a)
    return i