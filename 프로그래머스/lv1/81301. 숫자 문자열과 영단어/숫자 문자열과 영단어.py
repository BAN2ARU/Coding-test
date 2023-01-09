def solution(s):
    
    for i, z in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        s = s.replace(z,str(i))
    
    return int(s)