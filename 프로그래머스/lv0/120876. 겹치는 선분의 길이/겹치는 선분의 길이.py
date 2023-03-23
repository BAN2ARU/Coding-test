def solution(lines):
    llist = [set(range(line[0], line[1])) for line in lines]
    return len((llist[0] & llist[1]) | (llist[2] & llist[1]) | (llist[0] & llist[2]))