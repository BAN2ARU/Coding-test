def solution(myString, pat):
    num = len(pat)
    for n in range(1, len(myString)+1) :
        if pat in myString[-n:] :
            if (-n+len(pat)) == 0 :
                return myString
            return(myString[:-n+len(pat)])