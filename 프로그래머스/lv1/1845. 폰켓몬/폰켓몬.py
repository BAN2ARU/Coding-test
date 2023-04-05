def solution(nums):
    cnt = len(nums) // 2
    uni = len(set(nums))
    return min(cnt, uni)