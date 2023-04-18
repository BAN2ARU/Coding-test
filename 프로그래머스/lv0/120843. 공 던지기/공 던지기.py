def solution(numbers, k):
    numbers = numbers * 2
    numbers = numbers[::2]
    return numbers[k%len(numbers)-1]