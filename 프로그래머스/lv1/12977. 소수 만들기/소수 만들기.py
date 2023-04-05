def solution(nums):
    answer = 0
    for i in range(len(nums)-2) :
        for j in range(i+1, len(nums)-1) :
            for k in range(j+1, len(nums)) :
                num = nums[i] + nums[j] + nums[k]
                for n in range(2, int(num**0.5)+1) :
                    if num % n == 0 :
                        break
                    elif n == int(num**0.5) :
                        answer+=1
    return answer