def solution(a, b):
    answer = 0
    gcm = lambda x,y: y if x%y == 0 else gcm(y, x%y)
    gcm_v = gcm(max(a,b), min(a,b))
    b = b // gcm_v

    
    for i in range(2, b//2 + 1) :
        if b % i == 0 :
            if i % 2 == 0 or i % 5 == 0: 
                continue
            return 2
    return 1 if b % 2 == 0 or b % 5 ==0 or b==1 else 2