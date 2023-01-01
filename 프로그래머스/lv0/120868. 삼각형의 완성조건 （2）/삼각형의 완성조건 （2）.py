def solution(sides):
    min_v = min(sides)
    max_v = max(sides)
    return 2*min_v-1 if min_v > 1 else min_v