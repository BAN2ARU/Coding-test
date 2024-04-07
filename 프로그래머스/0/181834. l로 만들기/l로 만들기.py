def solution(myString):
    for s in myString :
        if s in ['a','b','c','d','e','f','g','h','i','j','k'] :
            myString=myString.replace(s, 'l')
    return(myString)