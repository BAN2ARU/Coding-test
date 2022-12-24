def solution(age):
    alpha = ['a','b','c','d','e','f','g','h','i','j'] 
    answer = ''
    for i in str(age):
        answer += alpha[int(i)]
    return answer