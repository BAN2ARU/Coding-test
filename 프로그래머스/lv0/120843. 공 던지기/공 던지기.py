def solution(numbers, k):
    answers=[]
    if len(numbers)%2==0 :
        answers = numbers[::2]
    else :
        answers = numbers[::2] + numbers[1::2]
    return answers[k%len(answers)-1]